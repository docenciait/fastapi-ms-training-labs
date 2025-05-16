from fastapi import FastAPI
from app.interfaces.routes.users import router

app = FastAPI()
app.include_router(router)