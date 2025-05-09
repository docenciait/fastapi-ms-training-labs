from fastapi import FastAPI
from app.routers import products

app = FastAPI(title="Product Service")

app.include_router(products.router, prefix="/products", tags=["products"])
