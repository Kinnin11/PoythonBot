from application.Commands.Command import Command


class VariableMSGCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            irc.sendMessage(self.respondWith, stream)
