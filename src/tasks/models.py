from sqlalchemy import Column,Integer,Boolean,func,String,DateTime,ForeignKey
from src.utils.db import Base
from sqlalchemy.orm import Mapped

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
    product_id=Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))


class CartModel(Base):
    __tablename__="cart"

    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"),unique=True )
    created_at=Column(DateTime(timezone=True), server_default=func.now())


class CartItemsModel(Base):
    __tablename__="cartitems"

    id=Column(Integer, primary_key=True)
    product_id=Column(Integer, ForeignKey("products.id"),unique=True)
    price=Column(Integer)
    cart_id=Column(Integer, ForeignKey("cart.id"))

    quantity=Column(Integer)

class OrderItemsModel(Base):
    __tablename__="orderitems"

    id=Column(Integer, primary_key=True)
    product_id=Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    order_id=Column(Integer, ForeignKey("order.id", ondelete="CASCADE"))
    price=Column(Integer)


class OrderModel(Base):
    __tablename__="order"

    id= Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    status=Column(String, default="Pending")
    total_price= Column(Integer, nullable=False)



