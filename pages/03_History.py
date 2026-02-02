import streamlit as st
from database import get_user_history
import requests

st.title("📜 Riwayat Kreasi")

# Simulasi ID User (Nanti hubungkan dengan sistem login Supabase kamu)
# Untuk sementara kita pakai ID dummy jika belum ada session_state
user_id = st.session_state.get("user_id", "guest_user")

history = get_user_history(user_id)

if not history:
    st.info("Kamu belum memiliki riwayat kreasi. Mulailah di menu Studio!")
else:
    for item in history:
        with st.expander(f"🕒 {item['timestamp']} | Prompt: {item['prompt_text'][:30]}..."):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if item['image_url']:
                    st.image(item['image_url'], use_container_width=True)
            
            with col2:
                st.write(f"**Prompt:** {item['prompt_text']}")
                st.write(f"**Hasil Naskah:** {item['result_text']}")
                
                # Tombol Download Ulang
                img_data = requests.get(item['image_url']).content
                st.download_button(
                    label="💾 Download Ulang Gambar",
                    data=img_data,
                    file_name=f"history_{item['id']}.png",
                    mime="image/png",
                    key=f"btn_{item['id']}"
                )

st.divider()
