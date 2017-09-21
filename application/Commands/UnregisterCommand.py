from application.Commands.Command import Command


class UnregisterCommand(Command):
    def handle(self, user, stream, data, irc):
        from data.DataService import DataService
        if stream == '#poyobot':
            if Command.handle(self, user, stream, data, irc):
                mockList = irc.streamList
                i = 0
                for s in mockList:
                    if s.name[1:] == user:
                        irc.streamList.remove(mockList[i])
                        DataService.deleteStream(user, irc.streamList)
                        irc.sendMessage("{}, I have stopped sending poyo to your chat :(".format(user), stream)
                        return
                    i += 1
                irc.sendMessage("{}, I wasn't sending poyo to your chat to being with!".format(user), stream)
