from pydantic import BaseModel 



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