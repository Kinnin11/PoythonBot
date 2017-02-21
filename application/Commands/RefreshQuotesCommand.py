import Command


class RefreshQuotesCommand(Command):
    def handle(self, user, stream, data, irc):
        if super(RefreshQuotesCommand, self).handle(user, stream, data, irc):
            irc.refreshQuotes()
            irc.sendMessage('Quotes refreshed :)', stream)
