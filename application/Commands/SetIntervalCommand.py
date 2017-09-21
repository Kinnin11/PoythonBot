from application.Commands.Command import Command


class SetIntervalCommand(Command):
    def handle(self, user, stream, data, irc):
        if Command.handle(self, user, stream, data, irc):
            for s in irc.streamList:
                if s.name == stream:
                    try:
                        newInterval = int(data)
                        if newInterval < 3:
                            raise Exception
                        s.setInterval(newInterval)
                        irc.sendMessage('{}: your interval has been set to {}'.format(user, s.interval), stream)
                    except ValueError:
                        irc.sendMessage('Please enter only a number', stream)
                    except Exception:
                        irc.sendMessage('The interval must be above 3!', stream)
