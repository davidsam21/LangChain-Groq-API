from fastapi import FastAPI
from backend.routes.chat import router as chat_router
from backend.routes.vision import router as vision_router

app = FastAPI(title="Groq AI")

app.include_router(chat_router)
app.include_router(vision_router)