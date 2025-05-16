from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def list_users(self) -> List[User]:
        pass