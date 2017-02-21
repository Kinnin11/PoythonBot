import Command


class VariableMSGCommand(Command):
    def handle(self, user, stream, data, irc):
        if super(VariableMSGCommand, self).handle(user, stream, data, irc):
            irc.sendMessage(self.respondWith, stream)
