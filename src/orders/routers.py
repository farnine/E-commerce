from fastapi import APIRouter,Depends,status,Path
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.helpers import auth
from src.user.models import UserModel
from . import controllers
from .dtos import OrderResponseSchema,OrderItemsResponseSchema
from typing import Annotated

order_routes=APIRouter(prefix="/orders")

@order_routes.post("/", response_model=OrderItemsResponseSchema,status_code=status.HTTP_201_CREATED)
def create_orders_route(db:Session= Depends(get_db), user:UserModel=Depends(auth)):
    return controllers.create_orders(db,user)

@order_routes.get("/",response_model= list[OrderResponseSchema],status_code=status.HTTP_200_OK)
def view_order_route(db:Session= Depends(get_db), user:UserModel=Depends(auth)):
    return controllers.view_order(db,user)

@order_routes.get("/{order_id}", response_model=OrderItemsResponseSchema, status_code=status.HTTP_200_OK)
def view_single_order_route(
    order_id:int,
    db:Session=Depends(get_db), 
    user:UserModel=Depends(auth)):
    return controllers.view_single_order(order_id,db,user)


@order_routes.delete("/{order_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def cancel_order_route(order_id:Annotated[int, Path(gt=0)], db:Session=Depends(get_db), user:UserModel=Depends(auth)):
    return controllers.cancel_order(order_id, db, user)