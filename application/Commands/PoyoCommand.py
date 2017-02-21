import Command


class PoyoCommand(Command):
    def handle(self, user, stream, data, irc):
        if stream is not '#poyobot':
            if super(PoyoCommand, self).handle(user, stream, data, irc):
                irc.sendMessage(self.respondWith, stream)
