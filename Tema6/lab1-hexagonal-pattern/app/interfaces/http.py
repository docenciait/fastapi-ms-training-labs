from fastapi import APIRouter
from app.infrastructure.repository import InMemoryUserRepository

router = APIRouter()
repo = InMemoryUserRepository()

@router.get("/users")
def get_users():
    return repo.list_users()