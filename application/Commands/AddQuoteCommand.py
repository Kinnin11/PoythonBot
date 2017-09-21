from application.Commands.Command import Command


class AddQuoteCommand(Command):

    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            # DataService.saveQuote(data)
            irc.sendMessage('quote added :)', stream)
