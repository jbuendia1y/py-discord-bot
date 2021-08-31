from typing import List
from pydantic import BaseModel


class StoreItemBoost(BaseModel):
    amount: float
    stat: str


class StoreItem(BaseModel):
    name: str
    boost: StoreItemBoost
    cost: int


class StoreRackModel(BaseModel):
    type: str
    items: List[StoreItem]


class StoreModel(BaseModel):
    basic: StoreRackModel
    intermediate: StoreRackModel
    advanced: StoreRackModel
