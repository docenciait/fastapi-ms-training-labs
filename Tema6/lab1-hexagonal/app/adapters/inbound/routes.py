from fastapi import APIRouter
from app.adapters.outbound.repository import MariaDBUserRepository
from app.config.database import database

router = APIRouter()
repo = MariaDBUserRepository(database)

@router.get("/users")
async def get_users():
    return await repo.list_users()