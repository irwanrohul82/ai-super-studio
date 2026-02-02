import os
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def generate_all_assets(prompt):
    # 1. GENERATE TEKS (Menggunakan Groq - Llama 3)
    # Gratis, Super Cepat, dan Akurat
    try:
        groq_client = Groq(api_key=os.getenv("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"))
        text_res = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Buatkan naskah iklan pendek maksimal 15 kata untuk: {prompt}"}]
        )
        naskah = text_res.choices[0].message.content
    except Exception as e:
        naskah = f"Gagal generate teks: {str(e)}"

    # 2. GENERATE GAMBAR (Menggunakan Pollinations AI)
    # Gratis, Tanpa API Key, Unlimited
    # Kita buat prompt lebih detail agar hasilnya bagus
    formatted_prompt = prompt.replace(" ", "%20")
    img_url = f"https://image.pollinations.ai/prompt/{formatted_prompt}?width=1024&height=1024&nologo=true&seed=42"

    # 3. AUDIO (Tetap ElevenLabs jika masih ada kuota, atau skip jika tidak ada)
    # ElevenLabs memberikan 10.000 karakter gratis per bulan.
    audio_file = "output.mp3"
    try:
        from elevenlabs.client import ElevenLabs
        el_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
        audio = el_client.generate(text=naskah, voice="Rachel", model="eleven_multilingual_v2")
        with open(audio_file, "wb") as f:
            for chunk in audio: f.write(chunk)
    except:
        # Jika kuota ElevenLabs habis, buat file kosong agar tidak error
        with open(audio_file, "wb") as f: f.write(b"")

    return naskah, img_url, audio_file
