from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class StoreResponse(BaseModel):
    store_id: UUID
    mall_id: UUID
    name: str
    category: str
    floor: Optional[str]
    unit_number: Optional[str]
    hours: Optional[dict]
    contact: Optional[dict]

    model_config = {
        "from_attributes": True
    }

