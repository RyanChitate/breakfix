from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from Backend.db import get_db
from Backend.schemas.mall import MallCreate, MallResponse
from Backend.crud.mall import get_malls, create_mall


router = APIRouter(prefix="/malls", tags=["Malls"])

@router.get("/", response_model=List[MallResponse])
def list_malls(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_malls(db, skip=skip, limit=limit)

@router.post("/", response_model=MallResponse)
def add_mall(mall: MallCreate, db: Session = Depends(get_db)):
    return create_mall(db, mall)
