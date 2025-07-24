from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
import logging

from Backend.db import get_db, engine, Base
from Backend.models import MallStore
from Backend.schemas import StoreResponse, StoreCard

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from Backend.routes import mall  # Router for malls

# Create tables in Supabase if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="RoamWise API")

# Enable CORS (for React Native or web frontends)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(mall.router)

# Redirect root to Swagger UI
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# Log a nice startup message
@app.on_event("startup")
async def startup_event():
    logging.basicConfig(level=logging.INFO)
    logging.info("🚀 RoamWise API is running! Swagger docs: http://127.0.0.1:8000/docs")
