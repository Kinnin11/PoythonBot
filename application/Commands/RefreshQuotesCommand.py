from application.Commands.Command import Command


class RefreshQuotesCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            irc.refreshQuotes()
            irc.sendMessage('Quotes refreshed :)', stream)
