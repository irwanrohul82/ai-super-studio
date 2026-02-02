import streamlit as st

st.set_page_config(page_title="AI Super Studio", layout="wide")

st.markdown("# 🚀 AI Super Studio")
st.subheader("Ubah Ide Jadi Konten Viral Dalam 60 Detik")

st.write("Satu platform untuk Teks, Gambar, Suara, dan Video.")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔥 Mulai Sekarang (Gratis 50 Kredit)"):
        st.info("Silakan buka menu 'Studio' di sidebar.")
with col2:
    st.write("✅ Tanpa Biaya Langganan di Awal")
    st.write("✅ Hasil Kualitas Studio")

st.divider()
st.image("https://via.placeholder.com/800x400.png?text=Preview+Dashboard+AI", caption="Tampilan Dashboard Kreatif")