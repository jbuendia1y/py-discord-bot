class CommandModel:
    commands: list

    def __init__(self, object: dict) -> None:
        self.object = object
        self.commands = [func for func in object if callable(
            object[func]) and not func.startswith("__")]

    def exec_cmd(self, cmd: str):
        if cmd in self.commands:
            return self.object[cmd]
        else:
            raise Exception("The command not exist")
