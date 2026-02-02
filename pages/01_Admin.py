import streamlit as st
import pandas as pd
from database import get_admin_stats

st.title("🛡️ Admin Command Center")

try:
    users, logs = get_admin_stats()
    
    c1, c2 = st.columns(2)
    c1.metric("Total User", len(users))
    c2.metric("Total Kredit Terpakai", sum(l['cost_credits'] for l in logs))

    st.subheader("Daftar Penggunaan Terakhir")
    st.table(pd.DataFrame(logs).tail(10))
except:
    st.error("Koneksi Database Belum Terpasang.")
