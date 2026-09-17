from .dtos import ProductSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from .models import ProductModel
from src.user.models import UserModel
def get_all( db:Session):
    data = db.query(ProductModel).all()

    return data

def get_one(product_id:int, db:Session,user:UserModel):
    data= db.query(ProductModel).get(product_id)

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detial=" Product not found")

    return data

def create_product(body:ProductSchema, db:Session,user: UserModel):
    user_data=db.query(UserModel).filter(UserModel.id==user.id).first()
    
    if user_data.is_admin:
        data= ProductModel(
            name=body.name,
            description=body.description,
            price=body.price,
            is_available=body.is_available,
        )
        db.add(data)
        db.commit()
        db.refresh(data)

        return data


def update_product(product_id:int, body:ProductSchema, db:Session, user:UserModel):
    data= db.query(ProductModel).get(product_id)

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detial=" Product not found")

    body_dict=body.model_dump()

    for key, val in body_dict.items():
        setattr(data, key, val)

    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def partial_update_product():
    pass

def delete_product(product_id:int, db:Session, user:UserModel):
    data= db.query(ProductModel).get(product_id)
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detial=" Product not found")

    db.delete(data)
    db.commit()
    db.refresh(data)

    return None