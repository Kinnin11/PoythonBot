import Command


class CheckInterval(Command):
    def handle(self, user, stream, data, irc):
        if super(CheckInterval, self).handle(user, stream, data, irc):
            for s in irc.thread2.streamList:
                if s.name == stream:
                    irc.sendMessage('{}, Your interval is: {}'.format(user, s.getBaseInterval), stream)
