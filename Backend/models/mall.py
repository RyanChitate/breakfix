from sqlalchemy import Column, Integer, String
from Backend.db import Base

class Mall(Base):
    __tablename__ = "malls"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=True)

class MallStore(Base):
    __tablename__ = "mallstores"

    id = Column(Integer, primary_key=True, index=True)
    Store_Name = Column(String, nullable=False)
    Category = Column(String, nullable=False)
    Floor_Level = Column(Integer, nullable=False)
    Contact_Number = Column(String, nullable=True)
    Opening_Hours = Column(String, nullable=False)
    Closing_Hours = Column(String, nullable=False)
