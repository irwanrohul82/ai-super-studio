import streamlit as st
import pandas as pd
from database import get_admin_stats

st.set_page_config(page_title="Admin Panel", layout="wide")

st.title("🛡️ Admin Command Center")

try:
    # Mengambil data dari database.py
    users_data, logs_data = get_admin_stats()
    
    # Validasi jika data ada
    if users_data is not None and logs_data is not None:
        
        # --- BARIS 1: METRIK ---
        c1, c2, c3 = st.columns(3)
        
        total_users = len(users_data)
        total_credits = sum(item.get('cost_credits', 0) for item in logs_data)
        total_actions = len(logs_data)
        
        c1.metric("Total User Terdaftar", total_users)
        c2.metric("Total Kredit Terpakai", f"{total_credits} Pts")
        c3.metric("Total Generasi AI", total_actions)

        st.divider()

        # --- BARIS 2: TABEL LOGS ---
        st.subheader("📑 Aktivitas Pengguna Terbaru")
        if len(logs_data) > 0:
            df_logs = pd.DataFrame(logs_data)
            # Mengurutkan berdasarkan ID terbaru atau timestamp
            if 'timestamp' in df_logs.columns:
                df_logs['timestamp'] = pd.to_datetime(df_logs['timestamp'])
                df_logs = df_logs.sort_values(by='timestamp', ascending=False)
            
            # Menampilkan kolom yang penting saja agar rapi
            st.dataframe(
                df_logs[['timestamp', 'user_id', 'type', 'prompt_text', 'cost_credits']], 
                use_container_width=True
            )
        else:
            st.info("Belum ada aktivitas penggunaan yang tercatat.")

        # --- BARIS 3: DAFTAR USER ---
        st.subheader("👥 Data User")
        df_users = pd.DataFrame(users_data)
        st.table(df_users[['id', 'email', 'created_at']])

    else:
        st.warning("Koneksi berhasil, tetapi tabel di database mungkin kosong.")

except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat data: {e}")
    st.info("Pastikan Tabel 'profiles' dan 'usage_logs' sudah dibuat di Supabase.")
