from ..items import Equipment


class Equipped:
    armor: Equipment = None
    sword: Equipment = None

    def __init__(self, armor: Equipment = None, sword: Equipment = None) -> None:
        self.armor = armor
        self.sword = sword

    def get_equipped(self):
        return (self.armor, self.sword)
