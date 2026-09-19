from fastapi import FastAPI
from src.utils.db import Base,engine
from src.user.models import UserModel
from src.user.routers import user_routes
from src.tasks.models import ProductModel
from src.cart.models import CartModel,CartItemsModel
from src.orders.models import OrderModel,OrderItemsModel
from src.tasks.routers import task_routes
from src.catagory.models import CatagoryModel
from src.catagory.routers import catagory_routes


Base.metadata.create_all(engine)


app=FastAPI()

app.include_router(user_routes)
app.include_router(task_routes)
app.include_router(catagory_routes)