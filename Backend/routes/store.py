from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.store import Store
from schemas.store import StoreResponse
from typing import List
from uuid import UUID

router = APIRouter(prefix="/api/malls", tags=["Stores"])

@router.get("/{mall_id}/stores", response_model=List[StoreResponse])
def get_stores_for_mall(mall_id: UUID, db: Session = Depends(get_db)):
    stores = db.query(Store).filter(Store.mall_id == mall_id).all()
    if not stores:
        raise HTTPException(status_code=404, detail="No stores found for this mall.")
    return stores
