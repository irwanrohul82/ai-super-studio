import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("https://psmepcgqofdhidgcyyby.supabase.co")
key = os.getenv("sb_publishable_-340BVKwT_6W2H51MKZhww_EYfk-V_0")
supabase = create_client(url, key)

def log_usage(user_id, task_type, prompt, result, img_url, credits=1):
    data = {
        "user_id": user_id,
        "type": task_type,
        "prompt_text": prompt,
        "result_text": result,
        "image_url": img_url,
        "cost_credits": credits
    }
    try:
        supabase.table("usage_logs").insert(data).execute()
    except Exception as e:
        print(f"Gagal simpan database: {e}")

def get_user_history(user_id):
    res = supabase.table("usage_logs").select("*").eq("user_id", user_id).order("timestamp", desc=True).execute()
    return res.data

def get_admin_stats():
    users = supabase.table("profiles").select("*").execute()
    logs = supabase.table("usage_logs").select("*").execute()
    return users.data, logs.data
