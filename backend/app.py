import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Multimodal AI", layout="wide")
st.title("🧠 Multimodal AI System")

tab1, tab2 = st.tabs(["🗨️ Chat", "🖼️ Image → HTML/CSS"])

# ==================================================
# 🗨️ CHAT TAB
# ==================================================
with tab1:
    st.subheader("Chat with Groq AI")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="chat_input")

    if st.button("Send", key="chat_send"):
        if user_input:
            res = requests.post(
                f"{BACKEND_URL}/chat",
                json={"message": user_input}
            )

            if res.status_code == 200:
                ai_reply = res.json().get("response", "")
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("AI", ai_reply))
            else:
                st.error("Chat API error")

    for role, msg in st.session_state.chat_history:
        st.markdown(f"**{role}:** {msg}")

# ==================================================
# 🖼️ VISION TAB
# ==================================================
with tab2:
    st.subheader("Image → HTML/CSS Generator")

    uploaded_file = st.file_uploader(
        "Upload UI Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("Generate HTML/CSS", key="vision_generate"):
            with st.spinner("Processing with AI..."):
                res = requests.post(
                    f"{BACKEND_URL}/vision/image-to-html",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type
                        )
                    }
                )

            if res.status_code == 200:
                data = res.json()

                st.success("Generation completed!")

                # ----------- RUN INFO -----------
                if "run_dir" in data:
                    st.subheader("📁 Run Folder")
                    st.code(data["run_dir"])

                # ----------- VISION TEXT -----------
                if "vision_txt" in data:
                    st.subheader("📄 vision.txt")
                    st.code(data["vision_txt"])

                # ----------- HTML -----------
                if "html" in data:
                    st.subheader("🌐 HTML")
                    st.code(data["html"], language="html")

                # ----------- CSS -----------
                if "css" in data:
                    st.subheader("🎨 CSS")
                    st.code(data["css"], language="css")

                # ----------- LIVE PREVIEW -----------
                if "html" in data and "css" in data:
                    st.subheader("👀 Live Preview")
                    st.components.v1.html(
                        f"<style>{data['css']}</style>{data['html']}",
                        height=600,
                        scrolling=True
                    )
            else:
                st.error("Vision API error")
                st.text(res.text)