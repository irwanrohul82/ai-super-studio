import streamlit as st
import requests
from engine import generate_all_assets
from database import log_usage

st.title("🎨 Creative Studio")
prompt = st.text_input("Apa yang ingin kamu buat?", placeholder="Contoh: Kedai kopi futuristik di hutan")

if st.button("🚀 Generate Masterpiece"):
    if prompt:
        with st.spinner("Sedang meracik konten..."):
            naskah, img_url, audio_path = generate_all_assets(prompt)
            
            # Simpan ke Database History
            log_usage(st.session_state.user_id, "Full Gen", prompt, naskah, img_url)
            
            c1, c2 = st.columns(2)
            with c1:
                st.image(img_url, caption="Hasil Visual")
                img_data = requests.get(img_url).content
                st.download_button("💾 Download Gambar", img_data, "image.png", "image/png")

            with c2:
                st.write(f"**Naskah:** {naskah}")
                st.audio(audio_path)
                with open(audio_path, "rb") as f:
                    st.download_button("📥 Download Audio", f, "voiceover.mp3", "audio/mp3")
    else:
        st.warning("Isi prompt terlebih dahulu!")
