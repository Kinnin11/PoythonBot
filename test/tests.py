from application.Commands.RegisterCommand import RegisterCommand
from application.IRC.IRCHandler import IRCHandler

irc = IRCHandler()
RegisterCommand("!checkinterval", cooldown=0).handle("poyo", "#poyobot", "", irc)
# UnregisterCommand("!test", cooldown=0).handle("poyo","#poyobot","", irc)
