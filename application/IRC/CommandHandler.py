


class CommandHandler:
    commandList = None

    def handleCommand(self, message, user):
        from data.DataService import DataService
        commandList = DataService.loadCommands()
        test = message
        pass
