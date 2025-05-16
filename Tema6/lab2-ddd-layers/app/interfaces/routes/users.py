from fastapi import APIRouter
from app.infrastructure.repositories.in_memory_user_repo import InMemoryUserRepository
from app.application.use_cases.list_users import ListUsersUseCase

router = APIRouter()
repo = InMemoryUserRepository()
use_case = ListUsersUseCase(repo)

@router.get("/users")
def get_users():
    return use_case.execute()