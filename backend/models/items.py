from pydantic import BaseModel


class Boost_consumable(BaseModel):
    stat: str
    amount: int


class Item(BaseModel):
    name: str


class Consumable(Item, BaseModel):
    boost: Boost_consumable
