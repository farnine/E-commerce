from fastapi import Request,status,HTTPException,Depends
from sqlalchemy.orm import Session
import jwt 
from jwt.exceptions import InvalidTokenError,ExpiredSignatureError
from .settings import settings
from src.user.models import UserModel
from .db import get_db





def is_auth(request:Request, db:Session= Depends(Session)):
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
