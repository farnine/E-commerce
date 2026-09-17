from .dtos import UserSchema
from .models import UserModel
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from fastapi import HTTPException,status,Request
import jwt
from jwt.exceptions import ExpiredSignatureError,InvalidTokenError
from datetime import datetime,timedelta
from src.utils.settings import settings

password_hash=PasswordHash.recommended()


def verify_password(plain_password,hash_password):
    return password_hash.verify(plain_password,hash_password)


def make_password_hashed(password):
    return password_hash.hash(password)

def password_Validation(password,re_password):
    if password!=re_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Password does not match")
    if len(password)<8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Password length minimun 8")
    return password


def register_user(body:UserSchema, db:Session):
    is_user=db.query(UserModel).filter(UserModel.username==body.username).first()

    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already Exist" )
    is_email=db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already Exist" )
    


    password=password_Validation(body.password, body.re_password)
    
    hash_password=make_password_hashed(password)

    data=UserModel(
        fullname=body.fullname,
        username=body.username,
        hash_password=hash_password,
        email=body.email,
        is_admin=body.is_admin
    )

   

    db.add(data)
    db.commit()
    db.refresh(data)

    return data


def login(body:UserSchema, db:Session):
    user=db.query(UserModel).filter(UserModel.username==body.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong Credential")


    verify=verify_password(body.password,user.hash_password)
    if not verify:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong Credential")

    exp_time=datetime.now()+timedelta(minutes=settings.TOKEN_EXPIRY_TIME)

    token=jwt.encode(
        {
            "id":user.id,
            "username":user.username,
            "exp":exp_time
        },
        settings.SECRET_KEY,
        settings.ALGORITHM
    )

    return {
        "Msg":"Login Successfully",
        "token":token
    }

def is_auth(request:Request, db:Session):
    try:
        raw_token=request.headers.get("authorization")
        if not raw_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found")
        token=raw_token.split(" ")[-1]

        data=jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user= db.query(UserModel).filter(UserModel.username==data.get("username")).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not Found")

        return user
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Expired")

    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Error")
