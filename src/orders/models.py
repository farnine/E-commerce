from src.utils.db import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,func





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



