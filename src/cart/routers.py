from fastapi import APIRouter,status,Depends
from sqlalchemy.orm import Session 
from src.utils.db import get_db
from . import controllers
from .dtos import CartItemsSchema,CartItemsResponseSchema, CartResponseSchema,CartSchema,CartAllResponseSchema
from src.utils.helpers import auth
from src.user.models import UserModel

cart_routes=APIRouter(prefix="/products")

#Cart Endpoints

@cart_routes.post("/cart", response_model=CartResponseSchema, status_code=status.HTTP_201_CREATED)
def create_cart_routes( db:Session= Depends(get_db), user:UserModel= Depends(auth)):
    return controllers.create_cart(db,user)


@cart_routes.get("/cart", status_code=status.HTTP_200_OK)
def cart_get_all_routes(db:Session=Depends(get_db),user:UserModel= Depends(auth)):
    return controllers.get_all_items(db,user)

@cart_routes.delete("/cart", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def clear_cart_routes(db:Session= Depends(get_db), user:UserModel=Depends(auth)):
    return controllers.clear_cart(db,user)



# CartItems Endpoints

@cart_routes.get(
    "/cart-items",
    response_model=list[CartItemsResponseSchema],
    status_code=status.HTTP_200_OK
    )
def get_all_routes(db=Depends(get_db)):
    return controllers.get_all(db)



@cart_routes.get(
    "/cart-items/{cartItem_id}",
    response_model=CartItemsResponseSchema,
    status_code=status.HTTP_200_OK
    )
def get_one_routes(cartItem_id:int,db=Depends(get_db)):
    return controllers.get_one(cartItem_id,db)

@cart_routes.post(
        "/cart-items",
        status_code=status.HTTP_201_CREATED,
        response_model=CartItemsResponseSchema
        )
def create_route(body:CartItemsSchema, db:Session= Depends(get_db), user:UserModel= Depends(auth)):
    return controllers.create(body, db,user)


@cart_routes.put(
    "/cart-items/{cartItem_id}",
    response_model=CartItemsResponseSchema,
    status_code=status.HTTP_201_CREATED
    )
def update_routes(cartItem_id:int,body:CartItemsSchema, db:Session=Depends(get_db),user:UserModel= Depends(auth)):
    return controllers.update(cartItem_id,body,db,user)

@cart_routes.delete(
    "/cart-items/{cartItem_id}",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
    )
def delete_routes(cartItem_id:int, db:Session=Depends(get_db), user:UserModel= Depends(auth)):
    return controllers.removeItem(cartItem_id, db, user)