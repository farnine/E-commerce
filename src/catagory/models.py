from src.utils.db import Base
from sqlalchemy import Column,String,Integer,DateTime,func

class CatagoryModel(Base):
    __tablename__="catagories"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    description=Column(String)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    
