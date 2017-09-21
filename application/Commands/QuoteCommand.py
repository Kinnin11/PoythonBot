from application.Commands.Command import Command


class QuoteCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            s = irc.get_stream(stream)
            if s is not None and s.getQuoteOption:
                return irc.sendMessage(irc.quoteService.getQuote(), stream)
