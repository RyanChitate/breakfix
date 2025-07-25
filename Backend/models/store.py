from sqlalchemy import Column, String, Text, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from db import Base

class Store(Base):
    __tablename__ = "stores"

    store_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mall_id = Column(UUID(as_uuid=True), ForeignKey("malls.mall_id"), nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    floor = Column(String)
    unit_number = Column(String)
    hours = Column(JSON)
    contact = Column(JSON)
