from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.cart.models import CartModel,CartItemsModel
from src.tasks.models import ProductModel
from .models import OrderItemsModel,OrderModel


def create_orders(db:Session, user:UserModel):
    # Check if the Cart is present
    cart= db.query(CartModel).filter(CartModel.user_id==user.id).first()
    print(cart.id)

    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    # Check if the cart-items is present
    
    items=db.query(CartItemsModel).filter(CartItemsModel.cart_id==cart.id).all()

    if not items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Items not found")

    total_price=0.0

    # Check: Product avialibility, Compare Quantity with Stock, Calculate total Price
    for item in items:
        product= db.query(ProductModel).filter(ProductModel.id==item.product_id).first()

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        if not product.is_available:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{product.name} not available")
        if item.quantity> product.stock:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not enough stock of {product.name} is available")
        total_price += float(item.price) * item.quantity

    #Create order
    order=OrderModel(
        user_id=user.id,
        total_price=float(total_price)
    )
    db.add(order)
    # Get order.id before creating OrderItems
    db.flush()

    #create order-item
    for item in items:
        order_item=OrderItemsModel(
            product_id=item.product_id,
            order_id=order.id,
            price=float(item.price),
            quantity=item.quantity
        )
        db.add(order_item)

        product = db.query(ProductModel).filter(ProductModel.id == item.product_id).first()
        if product:
            product.stock -= item.quantity

    #Clear Cart
    for item in items:
        db.delete(item)

    #Save everything
    db.commit()
    db.refresh(order)

    return order


# View Orders

def view_order(db:Session, user:UserModel):
    
    order= db.query(OrderModel).filter(OrderModel.user_id==user.id).all()
    

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Order not found"
        )
    return order

def view_single_order(order_id:int, db:Session, user:UserModel):
    order=db.query(OrderModel).filter(
        OrderModel.id==order_id,
        OrderModel.user_id==user.id
    ).first()

    if not order:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Order not found")

    return order


def cancel_order(order_id:int, db:Session, user:UserModel):
    order= db.query(OrderModel).filter(OrderModel.id==order_id).first()

    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

    db.delete(order)
    db.commit()

    return None

