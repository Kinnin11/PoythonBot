import Command
from data.DataService import DataService


class AddQuoteCommand(Command):
    def handle(self, user, stream, data, irc):
        if super(AddQuoteCommand, self).handle(user, stream, data, irc):
            DataService.saveQuote(data)
            irc.sendMessage('quote added :)', stream)
