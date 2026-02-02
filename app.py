import streamlit as st

st.set_page_config(page_title="AI Super Studio", layout="wide", page_icon="🚀")

st.markdown("# 🚀 AI Super Studio")
st.write("Satu klik untuk membuat konten Multimodal (Teks, Gambar, Audio).")

if "user_id" not in st.session_state:
    st.session_state["user_id"] = "guest_user_123" # ID Dummy untuk testing

st.info("Pilih menu **Studio** di sidebar kiri untuk mulai membuat konten!")

st.divider()
st.subheader("Fitur Unggulan:")
col1, col2, col3 = st.columns(3)
col1.write("🖼️ **AI Image Generation**")
col2.write("🔊 **Human-like Voiceover**")
col3.write("📝 **AI Copywriting**")
