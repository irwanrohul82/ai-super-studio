import os
import streamlit as st
from supabase import create_client
from dotenv import load_dotenv

# Memuat file .env jika ada (untuk penggunaan lokal)
load_dotenv()

# --- KONFIGURASI KONEKSI ---
# Mengambil variabel dari Streamlit Cloud Secrets atau file .env lokal
URL = st.secrets.get("https://psmepcgqofdhidgcyyby.supabase.co") or os.getenv("https://psmepcgqofdhidgcyyby.supabase.co")
KEY = st.secrets.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBzbWVwY2dxb2ZkaGlkZ2N5eWJ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk5OTY0ODQsImV4cCI6MjA4NTU3MjQ4NH0.VlAZEm_uMMETYRJU2axhpYFSjwcE5B4HFaHFSRi5jyI") or os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBzbWVwY2dxb2ZkaGlkZ2N5eWJ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk5OTY0ODQsImV4cCI6MjA4NTU3MjQ4NH0.VlAZEm_uMMETYRJU2axhpYFSjwcE5B4HFaHFSRi5jyI")

# Validasi Koneksi agar tidak terjadi crash 'redacted error'
if not URL or not KEY:
    st.error("❌ Konfigurasi Supabase tidak ditemukan!")
    st.info("Pastikan SUPABASE_URL dan SUPABASE_KEY sudah diisi di Secrets (online) atau .env (lokal).")
    st.stop()

# Inisialisasi Client Supabase
try:
    supabase = create_client(URL, KEY)
except Exception as e:
    st.error(f"❌ Gagal terhubung ke Supabase: {e}")
    st.stop()

# --- FUNGSI-FUNGSI DATABASE ---

def log_usage(user_id, task_type, prompt, result, img_url, credits=1):
    """Mencatat setiap pembuatan konten ke dalam tabel usage_logs."""
    data = {
        "user_id": user_id,
        "type": task_type,
        "prompt_text": prompt,
        "result_text": result,
        "image_url": img_url,
        "cost_credits": credits
    }
    try:
        return supabase.table("usage_logs").insert(data).execute()
    except Exception as e:
        print(f"Error log_usage: {e}")
        return None

def get_user_history(user_id):
    """Mengambil riwayat pembuatan konten milik user tertentu."""
    try:
        res = supabase.table("usage_logs") \
            .select("*") \
            .eq("user_id", user_id) \
            .order("timestamp", desc=True) \
            .execute()
        return res.data
    except Exception as e:
        print(f"Error get_user_history: {e}")
        return []

def get_admin_stats():
    """Mengambil data gabungan untuk halaman Admin Panel."""
    try:
        # Ambil semua data user dari tabel profiles
        users = supabase.table("profiles").select("*").execute()
        # Ambil semua log aktivitas dari tabel usage_logs
        logs = supabase.table("usage_logs").select("*").order("timestamp", desc=True).execute()
        
        return users.data, logs.data
    except Exception as e:
        print(f"Error get_admin_stats: {e}")
        return [], []

