from sqlalchemy import Column,Integer,Boolean,func,String,DateTime,ForeignKey,Float
from src.utils.db import Base
from sqlalchemy.orm import Mapped

class ProductModel(Base):
    __tablename__="products"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    description=Column(String)
    price=Column(Float, nullable=False)
    stock=Column(Integer, nullable=False)
    is_available=Column(Boolean)
    catagory_id=Column(Integer, ForeignKey("catagories.id", ondelete="CASCADE"), nullable=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())



