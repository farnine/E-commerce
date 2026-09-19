from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .dtos import CartItemsSchema
from src.tasks.models import ProductModel
from .models import CartItemsModel


def get_all(db:Session):
    data=db.query(CartItemsModel).all()


    return data

def get_one(cartItem_id: int, db:Session):
    data=db.query(CartItemsModel).get(cartItem_id)
    if not data:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    return data



def create(body:CartItemsSchema, db:Session):
    product=db.query(ProductModel).get(body.product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not found")

    data= CartItemsModel(
        product_id=product.id,
        price=product.price,
        cart_id=body.cart_id,
        quantity=body.quantity
    )

    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def update(cartItem_id: int,body:CartItemsSchema, db:Session):
    instance=db.query(CartItemsModel).get(cartItem_id)
    if not instance:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    body_dict=body.model_dump()

    for key,val in body_dict.items():
        setattr(instance,key, val)

    db.add(instance)
    db.commit()
    db.refresh(instance)

    return instance

def removeItem(cartItem_id,db:Session):
    data=db.query(CartItemsModel).get(cartItem_id)
    if not data:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    db.delete(data)
    db.commit()

    return None