import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("https://psmepcgqofdhidgcyyby.supabase.co")
key = os.getenv("sb_publishable_-340BVKwT_6W2H51MKZhww_EYfk-V_0")
supabase = create_client(url, key)

def register_user(email, password):
    return supabase.auth.sign_up({"email": email, "password": password})

def log_usage(user_id, task_type, credits):
    data = {
        "user_id": user_id,
        "type": task_type,
        "cost_credits": credits
    }
    supabase.table("usage_logs").insert(data).execute()

def get_admin_stats():
    users = supabase.table("profiles").select("*").execute()
    logs = supabase.table("usage_logs").select("*").execute()
    return users.data, logs.data
