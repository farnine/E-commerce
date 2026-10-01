from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.helpers import auth
from src.user.models import UserModel
from . import controllers


order_routes=APIRouter(prefix="/orders")

@order_routes.post("/")
def create_orders_route(db:Session= Depends(get_db), user:UserModel=Depends(auth)):
    return controllers.create_orders(db,user)