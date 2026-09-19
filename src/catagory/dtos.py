from pydantic import BaseModel,ConfigDict
from datetime import datetime

class CatagorySchema(BaseModel):
    name:str
    description:str



class CatagoryResponseSchema(BaseModel):
    id: int 
    name:str
    description:str
    created_at:datetime

    model_config=ConfigDict(from_attributes=True)