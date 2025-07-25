from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class MallResponse(BaseModel):
    mall_id: UUID
    name: str
    description: Optional[str]
    location: Optional[str]
    address: Optional[str]
    contact_info: Optional[dict]
    opening_hours: Optional[dict]
    map_image_url: Optional[str]

    model_config = {
        "from_attributes": True
    }
