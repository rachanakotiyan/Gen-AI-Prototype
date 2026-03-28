from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles   #add
from routes.chat import router as chat_router
from db.mongo import connect_db, disconnect_db

app = FastAPI(title="ET AI Concierge", version="1.0")

@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()

app.include_router(chat_router, prefix="/api")
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def root():
    return {"status": "ET Concierge is live"}
