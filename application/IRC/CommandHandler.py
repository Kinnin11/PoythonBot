from data.DataService import DataService


class CommandHandler:
    commandList = DataService.getCommandList()

    def __init__(self):
