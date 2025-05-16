from typing import List
from app.application.ports import UserRepository
from app.domain.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = [User(id=1, name="Alice"), User(id=2, name="Bob")]

    def list_users(self) -> List[User]:
        return self.users