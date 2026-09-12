from pydantic import BaseModel,ConfigDict
from datetime import datetime

class UserSchema(BaseModel):

    fullname:str | None = None
    username:str
    password:str
    re_password:str
    email:str


class UserResponseSchema(BaseModel):
    id:int
    fullname:str
    username:str
    
    email:str
    created_at: datetime
    updated_at:datetime

    model_config=ConfigDict(from_attributes=True)


class LoginSchema(BaseModel):
    username:str
    password:str