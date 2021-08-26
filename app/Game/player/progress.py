class Progress:
    lvl: int
    current_xp: int
    max_xp: int

    floor: int
    current_floor: int

    def __init__(self, lvl: int, current_xp: int, floor: int, current_floor: int = None) -> None:
        self.lvl = lvl
        self.current_xp = current_xp
        self.floor = floor
        self.current_floor = current_floor or 1

        self.calculate_xp()

    def calculate_xp(self):
        # Formula for now
        self.max_xp = round((2.5**(self.lvl**(1/len(str(self.lvl))))) * 100)

    def get_progress_text(self):
        # ** ** como en markdown
        return f"**Level**: {self.lvl}\n**XP**: {self.current_xp} / {self.max_xp}\n**Floor**: {self.floor}"
