from application.Commands.Command import Command
from application.Commands.UserLevel import UserLevel


class AddQuoteCommand(Command):
    def __init__(self):
        Command.__init__(self, "!addqoute", userlevel=UserLevel.Kinnin11)

    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            # DataService.saveQuote(data)
            irc.sendMessage('quote added :)', stream)
