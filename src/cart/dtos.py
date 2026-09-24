from pydantic import BaseModel, field_validator
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

    @field_validator("quantity")
    @classmethod
    def check_quantity(cls, val:int)->int:
        if val<=0:
            raise ValueError("Quantity cannot zero")
        return val



class CartItemsResponseSchema(BaseModel):

    id:int
    product_id:int
    price:int
    cart_id:int
    quantity:int