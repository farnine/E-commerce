from fastapi import FastAPI
from src.utils.db import Base,engine
from src.user.models import UserModel
from src.user.routers import user_routes
from src.tasks.models import ProductModel,OrderModel,CartModel,OrderItemsModel,CartItemsModel,CatagoryModel
from src.tasks.routers import task_routes
Base.metadata.create_all(engine)


app=FastAPI()

app.include_router(user_routes)
app.include_router(task_routes)