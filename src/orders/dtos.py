from pydantic import BaseModel,ConfigDict


class OrderItemsResponseSchema(BaseModel):
    id:int
    price:float
    quantity:int

    model_config=ConfigDict(from_attributes=True)


class OrderResponseSchema(BaseModel):
    id:int
    status:str
    total_price:float
    items: list[OrderItemsResponseSchema]

    model_config = ConfigDict(from_attributes=True)