from fastapi import APIRouter, HTTPException
from typing import List
from app.models.order import Order
from app.db.memory_db import orders, get_all, get_item, add_item, update_item, delete_item
from app.db.memory_db import users, products

router = APIRouter()

@router.get("/", response_model=List[Order])
def list_orders():
    return get_all(orders)

@router.post("/", response_model=Order)
def create_order(order: Order):
    # Validate user exists
    if not get_item(users, order.user_id, 'user_id'):
        raise HTTPException(status_code=400, detail="User not found")
    # Validate products exist
    for pid in order.product_ids:
        if not get_item(products, pid, 'product_id'):
            raise HTTPException(status_code=400, detail=f"Product {pid} not found")
    return add_item(orders, order)

@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int):
    existing = get_item(orders, order_id, 'order_id')
    if not existing:
        raise HTTPException(status_code=404, detail="Order not found")
    return existing

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, order: Order):
    updated = update_item(orders, order_id, order, 'order_id')
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@router.delete("/{order_id}", response_model=Order)
def delete_order(order_id: int):
    deleted = delete_item(orders, order_id, 'order_id')
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return deleted
