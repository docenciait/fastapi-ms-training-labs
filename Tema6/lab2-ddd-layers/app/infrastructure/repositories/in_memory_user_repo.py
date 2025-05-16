from typing import List
from app.domain.entities.user import User
from app.application.ports.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = [User(id=1, name="Alice"), User(id=2, name="Bob")]

    def list_users(self) -> List[User]:
        return self.users