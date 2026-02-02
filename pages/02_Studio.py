import streamlit as st
from engine import generate_all_assets

st.title("🎨 Creative Studio")
prompt = st.text_input("Apa yang ingin kamu buat hari ini?", "Mobil sport di Jakarta masa depan")

if st.button("🚀 Generate Masterpiece"):
    with st.spinner("Sedang meracik konten..."):
        naskah, img_url, audio_path = generate_all_assets(prompt)
        
        c1, c2 = st.columns(2)
        with c1:
            st.image(img_url, caption="Hasil Visual AI")
        with c2:
            st.write(f"**Naskah:** {naskah}")
            st.audio(audio_path)
            st.button("🎬 Generate Video (Pro Only)")
