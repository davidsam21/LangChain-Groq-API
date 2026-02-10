from fastapi import APIRouter, UploadFile, File
import shutil
import os
from backend.services.vision_service import image_to_html_css

router = APIRouter(prefix="/vision", tags=["Vision"])

@router.post("/image-to-html")
async def image_to_html(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)   # 👈 THIS LINE FIXES IT

    file_path = f"temp/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = image_to_html_css(file_path)
    return result