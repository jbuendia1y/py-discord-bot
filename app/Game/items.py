class Rpg_object:
    name: str
    amount: int

    def __init__(self, name: str) -> None:
        self.name = name
        self.amount = 1


class Consumable:
    name: str
    boost: dict

    def __init__(self, name: str, boost: dict) -> None:
        self.name = name
        self.boost = boost

    def use(self) -> tuple:
        return (self.boost["stat"], self.boost["amount"])


class Equipment:
    name: str
    boost: dict

    def __init__(self, name: str, boost: dict) -> None:
        self.name = name
        self.boost = boost

    def get_stat(self) -> tuple:
        return (self.boost["stat"], self.boost["amount"])
