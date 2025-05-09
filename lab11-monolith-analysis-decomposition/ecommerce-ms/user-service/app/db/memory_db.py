from typing import List, Any
from app.models.user import User

# In-memory store
users: List[User] = []

def get_all(collection: List[Any]) -> List[Any]:
    return collection

def get_item(collection: List[Any], item_id: int, id_attr: str) -> Any:
    for item in collection:
        if getattr(item, id_attr) == item_id:
            return item
    return None

def add_item(collection: List[Any], item: Any) -> Any:
    collection.append(item)
    return item

def update_item(collection: List[Any], item_id: int, new_item: Any, id_attr: str) -> Any:
    for idx, item in enumerate(collection):
        if getattr(item, id_attr) == item_id:
            collection[idx] = new_item
            return new_item
    return None

def delete_item(collection: List[Any], item_id: int, id_attr: str) -> Any:
    for idx, item in enumerate(collection):
        if getattr(item, id_attr) == item_id:
            return collection.pop(idx)
    return None
