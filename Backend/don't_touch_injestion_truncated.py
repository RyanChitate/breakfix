import pandas as pd
from sqlalchemy import create_engine, text
from models import Base
from db import SQLALCHEMY_DATABASE_URL

# === Step 1: Load CSV ===
csv_file = "./malls/mall_data.csv"
df = pd.read_csv(csv_file, dtype={"Contact_Number": str})

# === Step 2: Connect to Supabase DB ===
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# === Step 3: Create table (if not exists) ===
Base.metadata.create_all(bind=engine)

# === Step 4: (Optional) Truncate table and reset ID ===
with engine.connect() as conn:
    conn.execute(text("TRUNCATE mall RESTART IDENTITY;"))
    conn.commit()

# === Step 5: Insert data ===
df.to_sql("mall", con=engine, if_exists="append", index=False)

# === Done ===
print(f"✅ Inserted {len(df)} rows into 'mall' table (IDs reset).")
