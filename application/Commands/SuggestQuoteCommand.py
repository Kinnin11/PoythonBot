from application.Commands.Command import Command
from data.DataService import DataService


class SuggestQuoteCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            DataService.saveSuggestion(data)
            irc.sendMessage('suggestion added :)', stream)
