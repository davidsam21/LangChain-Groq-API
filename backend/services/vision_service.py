import os
import shutil
from datetime import datetime
from backend.ai.vision_client import extract_text_from_image
from backend.services.chat_service import ask_ai

BASE_OUTPUT_DIR = "backend/generated"

def image_to_html_css(image_path: str):
    # Create unique run folder
    run_id = datetime.now().strftime("run_%Y%m%d_%H%M%S")
    run_dir = os.path.join(BASE_OUTPUT_DIR, run_id)
    os.makedirs(run_dir, exist_ok=True)

    # Copy input image for traceability
    image_name = os.path.basename(image_path)
    saved_image_path = os.path.join(run_dir, image_name)
    shutil.copy(image_path, saved_image_path)

    # 1. OCR
    vision_text = extract_text_from_image(image_path)

    # Save vision.txt
    vision_file_path = os.path.join(run_dir, "vision.txt")
    with open(vision_file_path, "w", encoding="utf-8") as f:
        f.write(vision_text)

    # 2. Prompt
    prompt = f"""
You are a senior frontend developer.

Convert the following UI description into clean HTML and CSS.
Return the result in this format:

--- index.html ---
<full html>

--- styles.css ---
<full css>

Text:
{vision_text}
"""

    # 3. LLM
    response = ask_ai(prompt)

    # 4. Parse & save HTML/CSS
    html_path = os.path.join(run_dir, "index.html")
    css_path = os.path.join(run_dir, "styles.css")

    html_content = ""
    css_content = ""

    if "--- index.html ---" in response and "--- styles.css ---" in response:
        parts = response.split("--- styles.css ---")
        html_content = parts[0].replace("--- index.html ---", "").strip()
        css_content = parts[1].strip()
    else:
        html_content = response  # fallback

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)

    return {
        "run_id": run_id,
        "run_dir": run_dir,
        "files": {
            "input_image": saved_image_path,
            "vision_txt": vision_file_path,
            "html": html_path,
            "css": css_path
        }
    }