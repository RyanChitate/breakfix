from sqlalchemy.orm import Session
from app.models.mall import Mall
from app.schemas.mall import MallCreate

def get_malls(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Mall).offset(skip).limit(limit).all()

def create_mall(db: Session, mall: MallCreate):
    db_mall = Mall(**mall.dict())
    db.add(db_mall)
    db.commit()
    db.refresh(db_mall)
    return db_mall
