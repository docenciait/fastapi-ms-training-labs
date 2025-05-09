from fastapi import APIRouter, HTTPException
from typing import List
from app.models.product import Product
from app.db.memory_db import products, get_all, get_item, add_item, update_item, delete_item

router = APIRouter()

@router.get("/", response_model=List[Product])
def list_products():
    return get_all(products)

@router.post("/", response_model=Product)
def create_product(product: Product):
    if get_item(products, product.product_id, 'product_id'):
        raise HTTPException(status_code=400, detail="Product already exists")
    return add_item(products, product)
