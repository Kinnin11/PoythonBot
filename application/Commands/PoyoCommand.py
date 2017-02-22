from application.Commands.Command import Command


class PoyoCommand(Command):
    def handle(self, user, stream, data, irc):
        if stream is not '#poyobot':
            if Command.handle(self, user, stream, data, irc):
                irc.sendMessage(self.respondWith, stream)
