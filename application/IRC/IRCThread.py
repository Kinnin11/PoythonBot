import string
import threading

from data.DataService import DataService


class IRCThread(threading.Thread):
    s = None
    commandList = None
    irc = None

    def __init__(self, socket, irc):
        super(IRCThread, self).__init__()
        self.s = socket
        self.irc = irc
        self.commandList = DataService.loadCommands()

    def run(self):
        readbuffer = ''
        while True:
            readbuffer = readbuffer + self.s.recv(1024)
            temp = string.split(readbuffer, "\n")
            readbuffer = temp.pop()
            print(temp[0])

            for line in temp:
                # Checks whether the message is PING because its a method of Twitch to check if you're afk
                if line[0] in "PING":
                    line = string.split(line, ' ')
                    print "PONG %s\r\n" % line[1]
                    self.s.send("PONG %s\r\n" % line[1])
                else:
                    # Splits the given string so we can work with it better
                    parts = string.split(line, ":")
                    if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                        try:
                            # Sets the message variable to the actual message sent
                            message = parts[2][:len(parts[2]) - 1]
                        except:
                            message = ''
                        # Sets the username variable to the actual username
                        usernamesplit = string.split(parts[1], "!")
                        username = usernamesplit[0]
                        stream = string.split(parts[1], ' ')[2]
                        # if message is a command take it to the commandhandler
                        if '!' in message[0]:
                            # splitting command and data
                            spit = str.split(message, ' ', 1)
                            command = spit[0]
                            data = ''
                            if len(spit) > 1:
                                data = spit[1]
                            self.handleCommand(command, data, username, stream)

    # checks if command exists and lets them handle the rest
    def handleCommand(self, command, data, user, stream):
        for s in self.commandList:
            if command in s.respondTo:
                s.handle(user, stream, data, self.irc)
