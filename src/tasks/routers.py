from fastapi import Depends,status,APIRouter
from .dtos import ProductResponseSchema,ProductSchema
from sqlalchemy.orm import Session
from . import controllers
from src.utils.db import get_db

task_routes=APIRouter(prefix="/tasks")

#list
@task_routes.get(
    "/products", 
    status_code=status.HTTP_200_OK,
    response_model=list[ProductResponseSchema]
    )
def get_all_products_routes(db:Session= Depends(get_db)):
    return controllers.get_all(db)


#Retrieve
@task_routes.get(
    "/products/product_id", 
    status_code=status.HTTP_200_OK,
    response_model=ProductResponseSchema
    )
def get_one_products_routes(product_id: int,db:Session= Depends(get_db)):
    return controllers.get_one(product_id,db)

#Create

@task_routes.post(
    "/products", 
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponseSchema
    )
def create_product_routes(body: ProductSchema,db:Session= Depends(get_db)):
    return controllers.create_product(body,db)

#Update
@task_routes.put(
    "/products/product_id", 
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponseSchema
    )
def update_product_routes(product_id: int,body:ProductSchema, db:Session= Depends(get_db)):
    return controllers.create_product(product_id,body,db)


#delete
@task_routes.delete(
    "/products/product_id", 
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None
    )
def delete_product_routes(product_id: int,db:Session= Depends(get_db)):
    return controllers.delete_product(product_id,db)
