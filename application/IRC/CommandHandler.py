from data.DataService import DataService


class CommandHandler:
    commandList = DataService.getCommandList()

    def handleCommand(self, message, user):
        test = message
        pass
