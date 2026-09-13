from sqlalchemy import Column,Integer,Boolean,func,String,DateTime
from src.utils.db import Base



class ProductModel(Base):
    __tablename__="products"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    description=Column(String)
    price=Column(Integer, nullable=False)
    is_available=Column(Boolean)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class CatagoryModel(Base):
    __tablename__="catagories"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())


class CartModel(Base):
    __tablename__="carts"

    id=Column(Integer, primary_key=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now())


class CartItemsModel(Base):
    __tablename__="cartitems"

    id=Column(Integer, primary_key=True)
    quantity=Column(Integer)

class OrderItemsModel(Base):
    __tablename__="orderitems"

    id=Column(Integer, primary_key=True)
    product_id=Column(Integer)
    order_id=Column(Integer)
    price=Column(Integer)


class OrderModel(Base):
    __tablename__="order"

    id= Column(Integer, primary_key=True)
    user_id=Column(Integer)
    status=Column(String, default="Pending")
    total_price= Column(Integer, nullable=False)

