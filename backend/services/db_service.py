from db.mongo import get_db
from datetime import datetime

async def upsert_profile(user_id: str, profile_data: dict):
    db = get_db()
    profile_data["user_id"] = user_id
    profile_data["updated_at"] = datetime.utcnow()
    # Only update fields that are not None
    update_fields = {k: v for k, v in profile_data.items() if v is not None and v != [] and v != "null"}
    await db.profiles.update_one(
        {"user_id": user_id},
        {"$set": update_fields},
        upsert=True
    )

async def get_profile(user_id: str) -> dict:
    db = get_db()
    profile = await db.profiles.find_one({"user_id": user_id}, {"_id": 0})
    return profile or {}

async def save_chat(user_id: str, user_message: str, bot_response: str):
    db = get_db()
    await db.chats.insert_one({
        "user_id": user_id,
        "user_message": user_message,
        "bot_response": bot_response,
        "timestamp": datetime.utcnow()
    })

async def get_chat_history(user_id: str, limit: int = 5) -> list:
    db = get_db()
    cursor = db.chats.find(
        {"user_id": user_id},
        {"_id": 0}
    ).sort("timestamp", -1).limit(limit)
    history = await cursor.to_list(length=limit)
    return list(reversed(history))
