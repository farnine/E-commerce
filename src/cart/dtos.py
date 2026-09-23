from pydantic import BaseModel 
from datetime import datetime
#Cart Schema's

class CartSchema(BaseModel):
    user_id:int

class CartResponseSchema(BaseModel):
    id:int 
    user_id:int
    created_at:datetime


class CartAllResponseSchema(BaseModel):
    id:int
    items:list


#CartItems Schema's

class CartItemsSchema(BaseModel):
    
    product_id:int
    price:int
    cart_id:int
    quantity:int

class CartItemsResponseSchema(BaseModel):

    id:int
    product_id:int
    price:int
    cart_id:int
    quantity:int