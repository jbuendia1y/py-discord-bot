from discord import Embed


class Inventory:
    items: list
    consumables: list

    def __init__(self, items: list = None, consumables: list = None) -> None:
        self.items = items or []
        self.consumables = consumables or []

    def get_embed(self):
        embed = Embed(title="Inventory")
        items = ""

        if len(self.items) == 0:
            items = "You don't have items"
        else:
            for item in self.items:
                items = items + f"{item.name} \n"

        consumables = ""
        if len(self.consumables) == 0:
            consumables = "You don't have consumables"
        else:
            for consumable in self.consumables:
                consumables = consumables + f"{consumable.name} \n"

        embed.add_field(name="Items", value=items)
        embed.add_field(name="Consumables", value=consumables)
        return embed

    def get_item(self, item: str):
        for item_obj in self.items:
            if item_obj.name.lower() == item.lower().strip():
                return item_obj
        raise Exception("The item isn't in your inventory")

    def get_consumbale(self, consumable: str):
        for consumable_obj in self.consumables:
            if consumable_obj.name.lower() == consumable.lower().strip():
                return consumable_obj
        raise Exception("The consumable isn't in your inventory")
