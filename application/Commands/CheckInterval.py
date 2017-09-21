from application.Commands.Command import Command


class CheckInterval(Command):

    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            if stream == '#poyobot':
                for s in irc.streamList:
                    if s.name == user:
                        irc.sendMessage('{}, Your interval is: {}'.format(user, s.getBaseInterval()), stream)
            else:
                for s in irc.streamList:
                    if s.name == stream[0:]:
                        irc.sendMessage('{}, Your interval is: {}'.format(user, s.getBaseInterval()), stream)
