import Command


class RegisterCommand(Command):
    def handle(self, user, stream, data, irc):
        if stream is '#poyobot':
            if super(RegisterCommand, self).handle(user, stream, data, irc):
                irc.sendMessage(self.respondWith, stream)
