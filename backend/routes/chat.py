from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.chat_service import ask_ai

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    message: str

@router.post("")
def chat_endpoint(req: ChatRequest):
    response = ask_ai(req.message)
    return {"response": response}