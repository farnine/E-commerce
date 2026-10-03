from src.utils.db import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,func,Float
from sqlalchemy.orm import relationship 






class OrderItemsModel(Base):
    __tablename__="orderitems"

    id=Column(Integer, primary_key=True)
    product_id=Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    order_id=Column(Integer, ForeignKey("order.id", ondelete="CASCADE"))
    price=Column(Float, nullable=False)
    quantity=Column(Integer, nullable=False)
    order = relationship(
        "OrderModel",
        back_populates="items"
    )


class OrderModel(Base):
    __tablename__="order"

    id= Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    status=Column(String, default="Pending")
    total_price= Column(Float, nullable=False)
    items = relationship(
        "OrderItemsModel",
        back_populates="order"
    )



