from pydantic import BaseModel,ConfigDict,field_validator
from datetime import datetime

class ProductSchema(BaseModel):
    name:str
    description:str
    price:float
    stock:int
    is_available:bool

    @field_validator("price")
    @classmethod
    def check_negative(cls, val: float)-> float:
        if val<0:
            raise ValueError("price cannot be negative")
        return val
    
    @field_validator("stock")
    @classmethod
    def check_negative(cls, val: int)-> int:
        if val<0:
            raise ValueError("Stock cannot be negative")
        return val



class ProductResponseSchema(BaseModel):
    id:int
    name:str
    description:str
    price:int
    stock: int
    is_available:bool
    created_at:datetime
    updated_at:datetime

    model_config=ConfigDict(from_attributes=True)
