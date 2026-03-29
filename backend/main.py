from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles   #add
from routes.chat import router as chat_router
from db.mongo import connect_db, disconnect_db
import os
import sys

app = FastAPI(title="ET AI Concierge", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://et-genai.vercel.app", "*"], # Explicitly allow Vercel frontend, and keep wildcard for flexibility
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("\n" + "="*50)
    print("[STARTUP] Starting ET AI Concierge Backend")
    print("="*50)
    
    # Check environment variables
    env_vars = {
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
        "MONGODB_URL": os.getenv("MONGODB_URL"),
        "DB_NAME": os.getenv("DB_NAME"),
    }
    
    missing_vars = [k for k, v in env_vars.items() if not v]
    
    if missing_vars:
        print(f"[ERROR] Missing environment variables: {', '.join(missing_vars)}")
        print("Application will fail when processing requests!")
    else:
        print("[OK] All environment variables configured")
    
    # Try to connect to MongoDB
    try:
        await connect_db()
        print("[OK] MongoDB connection successful")
    except Exception as e:
        print(f"[ERROR] MongoDB connection failed: {str(e)}", file=sys.stderr)
        raise
    
    print("="*50 + "\n")

@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()

app.include_router(chat_router, prefix="/api")
# app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def root():
    return {"status": "ET Concierge is live"}

@app.get("/health")
async def health():
    """Health check endpoint - verify all env vars and dependencies"""
    checks = {
        "backend": "Running",
        "GOOGLE_API_KEY": "OK" if os.getenv("GOOGLE_API_KEY") else "MISSING",
        "MONGODB_URL": "OK" if os.getenv("MONGODB_URL") else "MISSING",
        "DB_NAME": "OK" if os.getenv("DB_NAME") else "MISSING",
    }
    
    all_good = all(v == "OK" or v == "Running" for v in checks.values())
    return {
        "status": "healthy" if all_good else "degraded",
        "checks": checks
    }
