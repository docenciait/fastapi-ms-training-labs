from fastapi import FastAPI
from app.routers import users, products, orders

app = FastAPI(title="ECommercePlatform Monolítico Funcional")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
