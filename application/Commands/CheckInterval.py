from application.Commands.Command import Command


class CheckInterval(Command):

    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            if stream == '#poyobot':
                s = irc.get_stream(user)
                if s is not None:
                    irc.sendMessage('{}, Your interval is: {}'.format(user, s.getBaseInterval()), stream)
            else:
                s = irc.get_stream(stream)
                if s is not None:
                    irc.sendMessage('{}, Your interval is: {}'.format(user, s.getBaseInterval()), stream)
