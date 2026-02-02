import os
import streamlit as st
from supabase import create_client
from dotenv import load_dotenv

# Memuat file .env jika ada (untuk penggunaan lokal)
load_dotenv()

# --- KONFIGURASI KONEKSI ---
# Mengambil variabel dari Streamlit Cloud Secrets atau file .env lokal
URL = st.secrets.get("https://psmepcgqofdhidgcyyby.supabase.co") or os.getenv("https://psmepcgqofdhidgcyyby.supabase.co")
KEY = st.secrets.get("sb_secret_iVXs7lUF4-eCsnF3-WXyRg_5DUYWHUP") or os.getenv("sb_secret_iVXs7lUF4-eCsnF3-WXyRg_5DUYWHUP")

if not url or not key:
    st.error("❌ Konfigurasi Supabase tidak ditemukan!")
    st.write("Daftar kunci yang terdeteksi di server:", list(st.secrets.keys()))
    st.stop()

supabase = create_client(url, key)
