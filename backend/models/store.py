from pydantic import BaseModel
from typing import List


class Boost(BaseModel):
    amount: float
    stat: str


class Store_item(BaseModel):
    name: str
    boost: Boost
    cost: int


class Store(BaseModel):
    type: str
    items: List[Store_item]
