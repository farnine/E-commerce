from fastapi import APIRouter,status,Depends,Request
from . import controllers
from src.utils.db import get_db
from sqlalchemy.orm import Session
from .dtos import UserSchema,UserResponseSchema,LoginSchema


user_routes=APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED )
def register_user_route(body:UserSchema, db: Session= Depends(get_db)):
    return controllers.register_user(body,db)

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login_routes(body:LoginSchema, db: Session=Depends(get_db)):
    return controllers.login(body,db)



@user_routes.get("/auth", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
def is_auth_routes(request:Request, db: Session=Depends(get_db)):
    return controllers.is_auth(request, db)