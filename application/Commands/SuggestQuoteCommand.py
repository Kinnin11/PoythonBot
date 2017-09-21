from application.Commands.Command import Command



class SuggestQuoteCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            from data.DataService import DataService
            DataService.saveSuggestion(data)
            irc.sendMessage('suggestion added :)', stream)
