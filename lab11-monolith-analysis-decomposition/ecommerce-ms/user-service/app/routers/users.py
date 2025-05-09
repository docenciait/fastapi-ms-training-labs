from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User
from app.db.memory_db import users, get_all, get_item, add_item, update_item, delete_item

router = APIRouter()

@router.get("/", response_model=List[User])
def list_users():
    return get_all(users)

@router.post("/", response_model=User)
def create_user(user: User):
    if get_item(users, user.user_id, 'user_id'):
        raise HTTPException(status_code=400, detail="User already exists")
    return add_item(users, user)
