from fastapi import FastAPI
from app.interfaces.http import router

app = FastAPI()
app.include_router(router)