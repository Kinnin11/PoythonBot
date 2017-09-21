from application.Commands.Command import Command


class QuoteOptionCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            from data.DataService import DataService
            for streamobj in irc.streamList:
                if streamobj.name == stream:
                    streamobj.setQuoteOption(data)
                    DataService.saveStreams(irc)
                    irc.sendMessage('quotes are now set to {}'.format(streamobj.getQuoteOption), stream)
