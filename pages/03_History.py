import streamlit as st
import requests
from database import get_user_history

st.title("📜 Riwayat Kreasi")

user_id = st.session_state.get("user_id", "guest_user_123")
history = get_user_history(user_id)

if not history:
    st.write("Belum ada riwayat.")
else:
    for item in history:
        with st.expander(f"🕒 {item['timestamp']} - {item['prompt_text'][:40]}..."):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(item['image_url'])
            with col2:
                st.write(f"**Naskah:** {item['result_text']}")
                img_data = requests.get(item['image_url']).content
                st.download_button("💾 Download Gambar", img_data, f"img_{item['id']}.png", "image/png", key=item['id'])
