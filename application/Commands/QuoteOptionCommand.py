from application.Commands.Command import Command


class QuoteOptionCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            from data.DataService import DataService
            streamobj = irc.get_stream(stream)
            if streamobj is not None:
                streamobj.setQuoteOption(data)
                DataService.saveStreams(irc)
                irc.sendMessage('quotes are now set to {}'.format(streamobj.getQuoteOption), stream)
