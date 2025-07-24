from db import engine

try:
    with engine.connect() as conn:
        print("✅ Successfully connected to Supabase Postgres!")
except Exception as e:
    print("❌ Failed to connect:", e)





