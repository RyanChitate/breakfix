from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.mall import Mall
from schemas.mall import MallResponse
from typing import List

router = APIRouter(prefix="/api/malls", tags=["Malls"])

@router.get("/", response_model=List[MallResponse])
def get_malls(db: Session = Depends(get_db)):
    return db.query(Mall).all()
