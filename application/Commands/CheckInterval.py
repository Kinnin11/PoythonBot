from application.Commands.Command import Command
from application.IRC import IRCHandler


class CheckInterval(Command):
    def __init__(self):
        Command.__init__(self, "!checkinterval")

    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, IRCHandler):
            for s in irc.streamList:
                if s.name == stream[0:]:
                    irc.sendMessage('{}, Your interval is: {}'.format(user, s.getBaseInterval()), stream)
