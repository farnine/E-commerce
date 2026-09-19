from src.utils.db import Base
from sqlalchemy import Column,String,Integer,func,DateTime,ForeignKey



class CartModel(Base):
    __tablename__="cart"

    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"),unique=True )
    created_at=Column(DateTime(timezone=True), server_default=func.now())


class CartItemsModel(Base):
    __tablename__="cartitems"

    id=Column(Integer, primary_key=True)
    product_id=Column(Integer, ForeignKey("products.id",ondelete="CASCADE"))
    price=Column(Integer)
    cart_id=Column(Integer, ForeignKey("cart.id", ondelete="CASCADE"))

    quantity=Column(Integer)