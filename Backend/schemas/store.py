from pydantic import BaseModel
from typing import List

class StoreCard(BaseModel):
    name: str
    category: str
    floor_level: int
    open_time: str
    close_time: str
    contact_info: str
    recommendations: str

class StoreResponse(BaseModel):
    question: str
    stores: List[StoreCard]

    class Config:
        from_attributes = True  # Pydantic v2 style

