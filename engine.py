import openai
import replicate
import os
from elevenlabs.client import ElevenLabs

def generate_all_assets(prompt):
    client = openai.OpenAI(api_key=os.getenv("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"))
    
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
    el_client = ElevenLabs(api_key=os.getenv("e5583c0ce46b42648986d9473f39e59d5c9986a59beb3fefc391cdf53f004412"))
    audio = el_client.generate(text=naskah, voice="Rachel", model="eleven_multilingual_v2")
    audio_file = "output.mp3"
    with open(audio_file, "wb") as f:
        for chunk in audio: f.write(chunk)


    return naskah, img_url, audio_file

