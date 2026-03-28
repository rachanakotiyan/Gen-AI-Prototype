from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_instance = MongoDB()

async def connect_db():
    db_instance.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    db_instance.db = db_instance.client[os.getenv("DB_NAME")]
    print("✅ MongoDB connected")

async def disconnect_db():
    db_instance.client.close()

def get_db():
    return db_instance.db
