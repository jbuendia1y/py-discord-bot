from .player import Player
# Turn 0 = Turn player1
# Turn 1 = Turn player2


class Battle:
    def __init__(self, player1: Player, player2: Player, turn: int = 0) -> None:
        self.player1 = player1
        self.player2 = player2
        self.turn = turn

    def start_battle(self) -> Player:
        while self.player1.stats.hp <= 0 or self.player2.stats.hp:
            hp1 = self.player1.stats.hp
            hp2 = self.player2.stats.hp

            win = self.verify_hp()
            if win != None:
                return win

            if self.turn == 0:
                self.player1.stats.hp = hp1 - self.player2.attack()
                self.turn = 1
            else:
                self.player2.stats.hp = hp2 - self.player1.attack()
                self.turn = 0
        return self.verify_hp()

    def verify_hp(self):
        hp1 = self.player1.stats.hp
        hp2 = self.player2.stats.hp
        if hp1 <= 0 or hp2 <= 0:
            if hp1 < hp2:
                return self.player2
            else:
                return self.player1
