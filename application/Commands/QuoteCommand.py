from application.Commands.Command import Command


class QuoteCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            for streamobj in irc.streamList:
                if streamobj.name == stream and streamobj.getQuoteOption:
                    return irc.sendMessage(irc.quoteService.getQuote(), stream)
