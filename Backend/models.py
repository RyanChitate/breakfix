from sqlalchemy import Column, Integer, String
from db import Base

class MallStore(Base):
    __tablename__ = "mall"

    id = Column(Integer, primary_key=True, index=True)
    Store_Name = Column(String)
    Category = Column(String)
    Floor_Level = Column(Integer)
    Contact_Number = Column(String)
    Opening_Hours = Column(String)
    Closing_Hours = Column(String)
