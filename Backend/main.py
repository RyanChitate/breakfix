from fastapi import FastAPI
from app.api import mall

app = FastAPI()

app.include_router(mall.router)

@app.get("/")
def root():
    return {"msg": "FastAPI connected to Supabase ✅"}
