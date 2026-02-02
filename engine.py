import os
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def generate_all_assets(prompt):
    # 1. Teks via Groq (Llama 3)
    try:
        groq_client = Groq(api_key=os.getenv("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"))
        text_res = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Buatkan naskah iklan singkat maksimal 15 kata untuk: {prompt}"}]
        )
        naskah = text_res.choices[0].message.content
    except:
        naskah = "Gagal memproses teks. Pastikan API Key Groq benar."

    # 2. Gambar via Pollinations (Gratis)
    formatted_prompt = prompt.replace(" ", "%20")
    img_url = f"https://image.pollinations.ai/prompt/{formatted_prompt}?width=1024&height=1024&nologo=true"

    # 3. Audio via ElevenLabs
    audio_file = "output.mp3"
    try:
        from elevenlabs.client import ElevenLabs
        el_client = ElevenLabs(api_key=os.getenv("sk_4a84d2e94cdf13bf6ce684ed4bc1f37fac6b213f914c06ee"))
        audio = el_client.generate(text=naskah, voice="Rachel", model="eleven_multilingual_v2")
        with open(audio_file, "wb") as f:
            for chunk in audio: f.write(chunk)
    except:
        with open(audio_file, "wb") as f: f.write(b"") # File kosong jika gagal

    return naskah, img_url, audio_file
