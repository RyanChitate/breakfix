from sqlalchemy import Column, String, Text, JSON, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from db import Base

class Mall(Base):
    __tablename__ = "malls"

    mall_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)  # Placeholder for Geography type
    address = Column(Text)
    contact_info = Column(JSON)
    opening_hours = Column(JSON)
    map_image_url = Column(Text)
    created_at = Column(TIMESTAMP)
