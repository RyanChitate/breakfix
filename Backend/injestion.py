import pandas as pd
from sqlalchemy import create_engine
from models import Base
from db import SQLALCHEMY_DATABASE_URL

# === Step 1: Load CSV with Contact_Number as string ===
csv_file = "./malls/MallWinnieMandelaCresent - WinnieMandelaCresent.csv"
df = pd.read_csv(csv_file, dtype={"Contact_Number": str})

# === Step 2: Connect to Supabase DB ===
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# === Step 3: Create table (if not already created) ===
Base.metadata.create_all(bind=engine)

# === Step 4: Insert data ===
df.to_sql("mall", con=engine, if_exists="append", index=False)

# === Done ===
print(f"✅ Inserted {len(df)} rows into 'mall' table.")
