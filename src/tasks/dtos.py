from pydantic import BaseModel,ConfigDict
from datetime import datetime

class ProductSchema(BaseModel):
    name:str
    description:str
    price:int
    is_available:bool


class ProductResponseSchema(BaseModel):
    id:int
    name:str
    description:str
    price:int
    is_available:bool
    created_at:datetime
    updated_at:datetime

    model_config=ConfigDict(from_attributes=True)
