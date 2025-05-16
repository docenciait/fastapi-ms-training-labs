from fastapi import FastAPI
from app.adapters.inbound.routes import router
from app.config.database import database

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()