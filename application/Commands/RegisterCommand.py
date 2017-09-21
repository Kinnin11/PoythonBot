import threading

from application.Commands.Command import Command
from application.SendPoyo.Stream import Stream


class RegisterCommand(Command):
    def handle(self, user, stream, data, irc):
        from data.DataService import DataService
        if stream == '#poyobot':
            if Command.handle(self, user, stream, data, irc):
                # looking up if user already exists
                for s in irc.streamList:
                    if s.name[1:] == user:
                        irc.sendMessage("{}, I'm already sending you poyo!".format(user), stream)
                # if non-existent, create
                newStream = Stream("#" + user, threading.Event(), irc)
                irc.streamList.append(newStream)
                DataService.addStream(newStream)
                irc.sendMessage("{}, I will now poyo in your chat every so often".format(user), stream)
