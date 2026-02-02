import streamlit as st
import requests
from engine import generate_all_assets

st.title("🎨 Creative Studio")
prompt = st.text_input("Apa yang ingin kamu buat hari ini?", "Mobil sport di Jakarta masa depan")

if st.button("🚀 Generate Masterpiece"):
    with st.spinner("Sedang meracik konten..."):
        naskah, img_url, audio_path = generate_all_assets(prompt)
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("🖼️ Hasil Visual")
            st.image(img_url, use_container_width=True)

            # ... di dalam blok if st.button("🚀 Generate Masterpiece"):
naskah, img_url, audio_path = generate_all_assets(prompt)

# SIMPAN KE HISTORY
from database import log_usage
user_id = st.session_state.get("user_id", "guest_user")
log_usage(user_id, "Full Generation", prompt, naskah, img_url)
            
            # --- FITUR DOWNLOAD GAMBAR ---
            try:
                img_data = requests.get(img_url).content
                st.download_button(
                    label="💾 Download Gambar",
                    data=img_data,
                    file_name="ai_image.png",
                    mime="image/png",
                    use_container_width=True
                )
            except:
                st.error("Gagal menyiapkan download gambar.")

        with c2:
            st.subheader("🔊 Voiceover & Naskah")
            st.write(f"**Naskah:** {naskah}")
            st.audio(audio_path)
            
            # --- FITUR DOWNLOAD AUDIO ---
            with open(audio_path, "rb") as file:
                st.download_button(
                    label="📥 Download Audio (MP3)",
                    data=file,
                    file_name="ai_voiceover.mp3",
                    mime="audio/mp3",
                    use_container_width=True
                )
            
            st.divider()
            st.button("🎬 Generate Video (Pro Only)")
