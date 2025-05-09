from pydantic import BaseModel
from typing import List

class Order(BaseModel):
    order_id: int
    user_id: int
    product_ids: List[int]
    status: str
