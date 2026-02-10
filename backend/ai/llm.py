from langchain_groq import ChatGroq
from backend.core.config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-Versatile",
    groq_api_key=GROQ_API_KEY
)