from fastapi import APIRouter,Depends,status
from . import controllers
from .models import CatagoryModel
from .dtos import CatagorySchema,CatagoryResponseSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.utils.db import get_db
from src.utils.helpers import auth 


catagory_routes=APIRouter(prefix="/products")

#List
@catagory_routes.get(
    "/catagories",
    response_model=list[CatagoryResponseSchema],
    status_code=status.HTTP_200_OK
    )
def get_all_routes(db:Session= Depends(get_db)):
    return controllers.get_all(db)


# Retrieve 
@catagory_routes.get(
    "/catagories/{catagories_id}",
    response_model=CatagoryResponseSchema,
    status_code=status.HTTP_200_OK
    )
def get_one_routes(
    catagories_id: int,
    db:Session= Depends(get_db),
    
    ):
    return controllers.get_one(catagories_id,db)


#Create 
@catagory_routes.post(
    "/catagories",
    response_model=CatagoryResponseSchema,
    status_code=status.HTTP_201_CREATED 
    )
def create_routes(
    body: CatagorySchema,
    db:Session= Depends(get_db),
    user:UserModel= Depends(auth)
    ):
    return controllers.create(body,db,user)


#Update
@catagory_routes.put(
    "/catagories/{catagories_id}",
    response_model=CatagoryResponseSchema,
    status_code=status.HTTP_201_CREATED
    )
def update_routes(
    catagories_id: int,
    body:CatagorySchema,
    db:Session= Depends(get_db),
    user:UserModel=Depends(auth)
    
    ):
    return controllers.update(catagories_id,body,db,user)

#Delete
@catagory_routes.delete(
    "/catagories/{catagories_id}",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
    )
def delete_routes(
    catagories_id: int,
    db:Session= Depends(get_db),
    user:UserModel=Depends(auth)
    
    ):
    return controllers.delete_catagory(catagories_id,db,user)