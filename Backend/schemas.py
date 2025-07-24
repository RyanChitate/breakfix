from pydantic import BaseModel
from typing import Optional, List

class StoreCard(BaseModel):
    name: str
    category: str
    floor_level: int
    open_time: str
    close_time: str
    contact_info: Optional[str] = None
    recommendations: str

class StoreResponse(BaseModel):
    question: str
    stores: List[StoreCard]
