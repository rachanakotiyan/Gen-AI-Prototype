from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid
import asyncio

from agents.profiling_agent import run_profiling_agent
from agents.intent_agent import run_intent_agent
from agents.recommendation_agent import run_recommendation_agent
from agents.action_agent import run_action_agent
from agents.response_agent import run_response_agent
from services.db_service import upsert_profile, get_profile, save_chat, get_chat_history

router = APIRouter()

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
async def chat(request: ChatRequest):
    try:
        user_id = request.user_id or str(uuid.uuid4())
        user_message = request.message

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
        profiling_result, intent = await asyncio.gather(
            run_profiling_agent(full_conversation),
            run_intent_agent(full_conversation)   # full context, not just latest message
        )

        # Merge profile — never overwrite known data with null
        merged_profile = {**existing_profile}
        for k, v in profiling_result.items():
            if v and v != "null" and v != [] and v != "":
                merged_profile[k] = v
        merged_profile["user_id"] = user_id
        merged_profile["conversation_turn"] = conversation_turn

        # --- Recommendations + action sequentially (action depends on recs) ---
        recommendations = await run_recommendation_agent(merged_profile, intent)

        top_rec = recommendations[0] if recommendations else {}
        action = await run_action_agent(merged_profile, intent, top_rec)

        # --- Response agent gets FULL context ---
        response_text = await run_response_agent(
            full_conversation,   # entire history, not just latest message
            merged_profile,
            recommendations,
            action
        )

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
        raise HTTPException(status_code=500, detail=str(e))


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
