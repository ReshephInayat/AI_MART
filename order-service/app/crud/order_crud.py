from sqlmodel import select, Session
from app.models.order_model import Order, OrderCreate, OrderUpdate
from datetime import datetime
from fastapi import HTTPException


def create_order(order: OrderCreate, session: Session):
    db_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order


def get_all_orders(session: Session):
    all_orders = session.exec(select(Order)).all()
    return all_orders


def get_order_by_id(order_id: int, session: Session):
    order = session.exec(select(Order).where(Order.id == order_id)).one_or_none()
    if order is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return order


def delete_order_by_id(order_id: int, session: Session):
    # Step 1: Get the Product by ID
    order = session.exec(select(Order).where(Order.id == order_id)).one_or_none()
    if order is None:
        raise HTTPException(status_code=404, detail="Product not found")
    # Step 2: Delete the Product
    session.delete(order)
    session.commit()
    return {"message": "Product Deleted Successfully"}


def update_order_by_id(
    order_id: int, to_update_order_data: OrderUpdate, session: Session
):
    # Step 1: Get the Product by ID
    order = session.exec(select(Order).where(Order.id == order_id)).one_or_none()
    if order is None:
        raise HTTPException(status_code=404, detail="Product not found")
    # Step 2: Update the Product
    order_data = to_update_order_data.model_dump(exclude_unset=True)
    order.sqlmodel_update(order_data)
    session.add(order_data)
    session.commit()
    return order
