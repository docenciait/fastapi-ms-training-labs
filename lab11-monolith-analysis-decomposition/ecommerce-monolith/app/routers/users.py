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

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    existing = get_item(users, user_id, 'user_id')
    if not existing:
        raise HTTPException(status_code=404, detail="User not found")
    return existing

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    updated = update_item(users, user_id, user, 'user_id')
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int):
    deleted = delete_item(users, user_id, 'user_id')
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted
