from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .dtos import CartItemsSchema,CartSchema
from src.tasks.models import ProductModel
from .models import CartItemsModel,CartModel
from src.user.models import UserModel


#Cart Logic 

def create_cart(db:Session, user:UserModel):
    is_user=db.query(CartModel).filter(CartModel.user_id==user.id).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already Found")

    data= CartModel(
        user_id=user.id
    )
    db.add(data)
    db.commit()
    db.refresh(data)

    return data


def get_all_items(db:Session, user:UserModel):

    cart= db.query(CartModel).filter(user.id==CartModel.user_id).first()
    
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart Not Found")
    items=db.query(CartItemsModel).filter(CartItemsModel.cart_id==cart.id).all()

    return {
        "id":cart.id,
        "items":items
    }





# CartItems logic
def get_all(db:Session):
    data=db.query(CartItemsModel).all()


    return data

def get_one(cartItem_id: int, db:Session):
    data=db.query(CartItemsModel).get(cartItem_id)
    if not data:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    return data



def create(body:CartItemsSchema, db:Session):
    cart= db.query(CartModel).filter(CartModel.id == body.cart_id).first()
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart Not found")
    
    product=db.query(ProductModel).get(body.product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not found")
    if body.quantity>product.stock:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantity must be less ")
    check_cartitems= db.query(CartItemsModel).filter(CartItemsModel.product_id==product.id).first()
    if check_cartitems:
        body_dict=body.model_dump()
        for key,val in body_dict.items():
            setattr(check_cartitems,key,val)

        db.add(check_cartitems)
        db.commit()
        db.refresh(check_cartitems)

        return check_cartitems

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