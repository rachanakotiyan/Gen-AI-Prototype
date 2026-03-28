from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

from agents.profiling_agent import run_profiling_agent
from agents.intent_agent import run_intent_agent
from agents.recommendation_agent import run_recommendation_agent
from agents.action_agent import run_action_agent
from agents.response_agent import run_response_agent
from services.db_service import upsert_profile, get_profile, save_chat, get_chat_history

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None  # If None, we create a new user

class ChatResponse(BaseModel):
    user_id: str
    response: str
    profile: dict
    recommendations: list
    next_action: dict

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Generate user_id if new user
        user_id = request.user_id or str(uuid.uuid4())
        user_message = request.message

        # --- STEP 1: Get existing profile + history for context ---
        existing_profile = await get_profile(user_id)
        chat_history = await get_chat_history(user_id, limit=4)
        
        # Build conversation context for profiling
        history_text = "\n".join([
            f"User: {c['user_message']}\nAssistant: {c['bot_response']}"
            for c in chat_history
        ])
        full_conversation = f"{history_text}\nUser: {user_message}".strip()

        # --- STEP 2: Run Agent Pipeline (parallel where possible) ---
        
        # Agent 1: Extract profile from conversation
        new_profile_data = await run_profiling_agent(full_conversation)
        
        # Merge with existing profile (don't overwrite known data)
        merged_profile = {**existing_profile, **{
            k: v for k, v in new_profile_data.items()
            if v and v != "null" and v != []
        }}
        merged_profile["user_id"] = user_id
        
        # Agent 2: Detect intent from current message
        intent = await run_intent_agent(user_message)
        
        # Agent 3: Generate recommendations
        recommendations = await run_recommendation_agent(merged_profile, intent)
        
        # Agent 4: Decide next action
        top_rec = recommendations[0] if recommendations else {}
        action = await run_action_agent(merged_profile, intent, top_rec)
        
        # Agent 5: Generate human-friendly response
        response_text = await run_response_agent(user_message, merged_profile, recommendations, action)
        
        # --- STEP 3: Persist data ---
        await upsert_profile(user_id, merged_profile)
        await save_chat(user_id, user_message, response_text)

        return ChatResponse(
            user_id=user_id,
            response=response_text,
            profile=merged_profile,
            recommendations=recommendations,
            next_action=action
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
    # Mock intent for direct recommendations call
    intent = {"primary_intent": "general_query", "urgency": "low", "topic": "general"}
    recs = await run_recommendation_agent(profile, intent)
    return {"user_id": user_id, "recommendations": recs}
