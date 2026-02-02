import openai
import replicate
import os
from elevenlabs.client import ElevenLabs

def generate_all_assets(prompt):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # 1. Teks (GPT-4o)
    text_res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Buatkan naskah iklan 1 kalimat: {prompt}"}]
    )
    naskah = text_res.choices[0].message.content

    # 2. Gambar (DALL-E 3)
    img_res = client.images.generate(
        model="dall-e-3",
        prompt=f"Cinematic realistic: {prompt}",
        size="1024x1024"
    )
    img_url = img_res.data[0].url

    # 3. Audio (ElevenLabs)
    el_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
    audio = el_client.generate(text=naskah, voice="Rachel", model="eleven_multilingual_v2")
    audio_file = "output.mp3"
    with open(audio_file, "wb") as f:
        for chunk in audio: f.write(chunk)

    return naskah, img_url, audio_file