from sqlalchemy import Column,String,Integer,Boolean,func,DateTime
from src.utils.db import Base


class UserModel(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True)
    fullname=Column(String)
    username=Column(String, nullable=False)
    hash_password=Column(String, nullable=False)
    email= Column(String, nullable=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())