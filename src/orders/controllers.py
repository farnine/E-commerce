from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.cart.models import CartModel,CartItemsModel
from src.tasks.models import ProductModel
from .models import OrderItemsModel,OrderModel


def create_orders(db:Session, user:UserModel):
    # Check if the Cart is present
    cart= db.query(CartModel).filter(CartModel.user_id==user.id).first()

    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    # Check if the cart-items is present
    items=db.query(CartItemsModel).filter(CartItemsModel.cart_id==cart.id).all()
    if not items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Items not found")

    
    total_price=0

    # Check: Product avialibility, Compare Quantity with Stock, Calculate total Price
    for item in items:
        product= db.query(ProductModel).filter(ProductModel.id==item.product_id).first()

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        if not product.is_available:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{product.name} not available")
        if item.quantity> product.stock:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not enough stock of {product.name} is available")
        total_price+=item.price*item.quantity

    #Create order
    order=OrderModel(
        user_id=user.id,
        total_price=total_price
    )
    db.add(order)
    # Get order.id before creating OrderItems
    db.flush()

    #create order-item
    for item in items:
        order_item=OrderItemsModel(
            product_id=item.product_id,
            order_id=order.id,
            price=item.price
        )
        db.add(order_item)
        

        product.stock-=item.quantity

    #Clear Cart
    for item in items:
        db.delete(item)

    #Save everything
    db.commit()
    db.refresh(order)

    return order

    
     