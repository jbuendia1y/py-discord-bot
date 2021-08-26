from discord import Embed
from helpers import api


def fetch_item(name: str, lvl: str) -> dict:
    store = api.get("/store")
    for item in store[lvl]:
        if item["name"].lower() == name.lower():
            return item
    raise Exception("Item cannot found")


def buy(purchase: dict, wallet: int):
    lvl = purchase["lvl"]
    name = purchase["name"]
    try:
        item = fetch_item(name, lvl)
        diference: int = wallet - item["cost"]
        if diference >= 0:
            return (item, diference)
        raise Exception("You don't have enough money")
    except Exception as e:
        raise e


class Store:
    basic: list
    intermediate: list
    advanced: list

    def __init__(self) -> None:
        self.basic = []
        self.intermediate = []
        self.advanced = []
        # Fetch Resources for the Store

    def buy(self, purchase: dict, money: int):
        purchase_lvl = purchase["lvl"]
        list_lvl: list = self.__getattribute__(purchase_lvl)
        for item in list_lvl:
            if item.name == purchase["name"]:
                diference = money - item.cost
                if diference >= 0:
                    return (item, diference)

        raise Exception("The item not exist", money)

    def get_store_embed(self) -> Embed:
        embed = Embed(title="Store")
        embed.add_field(name="")
