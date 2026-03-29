from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
import uuid
import asyncio
import time
from collections import defaultdict, deque
import sys
import traceback

from agents.profiling_agent import run_profiling_agent
from agents.intent_agent import run_intent_agent
from agents.recommendation_agent import run_recommendation_agent
from agents.action_agent import run_action_agent
from agents.response_agent import run_response_agent
from services.db_service import upsert_profile, get_profile, save_chat, get_chat_history

router = APIRouter()

# Basic in-memory rate limiting (per user_id and per IP)
RATE_LIMIT_REQUESTS = 20
RATE_LIMIT_WINDOW_SEC = 60
_rate_limit_store = defaultdict(deque)
_rate_limit_lock = asyncio.Lock()

async def check_rate_limit(key: str):
    now = time.time()
    window_start = now - RATE_LIMIT_WINDOW_SEC
    async with _rate_limit_lock:
        queue = _rate_limit_store[key]
        while queue and queue[0] < window_start:
            queue.popleft()
        if len(queue) >= RATE_LIMIT_REQUESTS:
            return False
        queue.append(now)
        return True

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    user_id: str
    response: str
    profile: dict
    recommendations: list
    next_action: dict
    conversation_turn: int

@router.post("/chat", response_model=ChatResponse)
async def chat(request: Request, payload: ChatRequest):
    try:
        user_id = payload.user_id or str(uuid.uuid4())
        user_message = payload.message

        client_ip = request.client.host if request.client else "unknown"

        # Rate limit per user & per IP
        user_key = f"user:{user_id}"
        ip_key = f"ip:{client_ip}"

        if not await check_rate_limit(user_key):
            raise HTTPException(status_code=429, detail="Too many requests for this user. Please wait.")
        if not await check_rate_limit(ip_key):
            raise HTTPException(status_code=429, detail="Too many requests from this IP. Please wait.")

        # --- Fetch existing state ---
        existing_profile, chat_history = await asyncio.gather(
            get_profile(user_id),
            get_chat_history(user_id, limit=6)
        )

        conversation_turn = len(chat_history) + 1

        # Build full conversation string for context-aware agents
        history_text = "\n".join([
            f"User: {c['user_message']}\nAssistant: {c['bot_response']}"
            for c in chat_history
        ])
        full_conversation = f"{history_text}\nUser: {user_message}".strip()

        # --- Run profiling + intent IN PARALLEL ---
        try:
            profiling_result, intent = await asyncio.gather(
                run_profiling_agent(full_conversation),
                run_intent_agent(full_conversation)   # full context, not just latest message
            )
            print(f"✅ Profiling & Intent agents completed")
        except Exception as e:
            print(f"❌ Error in profiling/intent agents: {str(e)}", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            sys.stderr.flush()
            raise

        # Merge profile — never overwrite known data with null
        merged_profile = {**existing_profile}
        for k, v in profiling_result.items():
            if v and v != "null" and v != [] and v != "":
                merged_profile[k] = v
        merged_profile["user_id"] = user_id
        merged_profile["conversation_turn"] = conversation_turn

        # --- Recommendations + action sequentially (action depends on recs) ---
        try:
            recommendations = await run_recommendation_agent(merged_profile, intent)
            print(f"✅ Recommendation agent completed")
        except Exception as e:
            print(f"❌ Error in recommendation agent: {str(e)}", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            sys.stderr.flush()
            raise

        try:
            top_rec = recommendations[0] if recommendations else {}
            action = await run_action_agent(merged_profile, intent, top_rec)
            print(f"✅ Action agent completed")
        except Exception as e:
            print(f"❌ Error in action agent: {str(e)}", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            sys.stderr.flush()
            raise

        # --- Response agent gets FULL context ---
        try:
            response_text = await run_response_agent(
                full_conversation,   # entire history, not just latest message
                merged_profile,
                recommendations,
                action
            )
            print(f"✅ Response agent completed")
        except Exception as e:
            print(f"❌ Error in response agent: {str(e)}", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            sys.stderr.flush()
            raise

        # --- Persist ---
        await asyncio.gather(
            upsert_profile(user_id, merged_profile),
            save_chat(user_id, user_message, response_text)
        )

        return ChatResponse(
            user_id=user_id,
            response=response_text,
            profile=merged_profile,
            recommendations=recommendations,
            next_action=action,
            conversation_turn=conversation_turn
        )

    except Exception as e:
        error_details = traceback.format_exc()
        print(f"❌ ERROR in /chat endpoint:", file=sys.stderr)
        print(error_details, file=sys.stderr)
        sys.stderr.flush()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@router.get("/profile/{user_id}")
async def get_user_profile(user_id: str):
    profile = await get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/recommendations/{user_id}")
async def get_user_recommendations(user_id: str):
    profile = await get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    intent = {"primary_intent": "general_query", "urgency": "low", "topic": "general"}
    recs = await run_recommendation_agent(profile, intent)
    return {"user_id": user_id, "recommendations": recs}


@router.get("/history/{user_id}")
async def get_user_history(user_id: str):
    history = await get_chat_history(user_id, limit=20)
    if not history:
        raise HTTPException(status_code=404, detail="No history found")
    return {"user_id": user_id, "history": history}
