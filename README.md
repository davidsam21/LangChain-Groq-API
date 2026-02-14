# LangChain Groq Multimodal AI System

A multimodal AI system built using **LangChain** and the **Groq API**, featuring a **FastAPI backend** and a **Streamlit UI**.  
The project supports real-time LLM chat and vision-based **image-to-HTML/CSS generation** using a OCR served via Groq.

---

## 🚀 Features

- 💬 LLM Chat powered by Groq (via LangChain)
- 🖼️ Vision route: Convert UI images into HTML & CSS (OCR)
- ⚡ FastAPI backend with clean modular services
- 🎨 Streamlit frontend for Chat + Vision
- 🧠 Memory-enabled conversations
- 🔐 Secure environment-based configuration

---

## 🛠 Tech Stack

- Python
- LangChain
- Groq API
- OCR
- FastAPI
- Streamlit

---

## 📂 Project Structure

langchain_groq_api/
│
├── backend/
│ ├── ai/
│ ├── routes/
│ ├── services/
│ ├── models/
│ └── main.py
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/davidsam21/LangChain-Groq-API.git
cd LangChain-Groq-API

### 2️⃣ Create virtual environment

- python -m venv lib
- lib\Scripts\activate

### 3️⃣ Install dependencies

- pip install -r requirements.txt

### 4️⃣ Configure environment variables

Create a .env file:

- GROQ_API_KEY=your_groq_api_key

### ▶️ Run the Application

Start FastAPI backend
- uvicorn backend.main:app --reload

Start Streamlit UI
- streamlit run streamlit_app.py

### 📌 Notes

- Generated AI outputs are excluded from version control.
- Environment variables are securely managed.
- Designed for real-world scalability.

### 📜 License

This project is for educational and experimental purposes.
