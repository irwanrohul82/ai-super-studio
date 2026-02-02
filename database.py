import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
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