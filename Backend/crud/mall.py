from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from Backend.models.mall import Mall
from Backend.schemas.mall import MallCreate


def get_malls(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of malls with pagination."""
    return db.query(Mall).offset(skip).limit(limit).all()

def create_mall(db: Session, mall: MallCreate):
    """Create a new mall entry."""
    try:
        existing_mall = db.query(Mall).filter(Mall.name == mall.name).first()
        if existing_mall:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Mall '{mall.name}' already exists."
            )
        db_mall = Mall(**mall.dict())
        db.add(db_mall)
        db.commit()
        db.refresh(db_mall)
        return db_mall
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
