from typing import List
from app.domain.entities.user import User
from app.application.ports.user_repository import UserRepository

class ListUsersUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self) -> List[User]:
        return self.repo.list_users()