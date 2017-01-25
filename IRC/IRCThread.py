import string
import threading

#Reads the chat and sends messages to CommandHandler

class IRCThread(threading.Thread):
    s = None
    def __init__(self, socket, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(IRCThread, self).__init__()
        self.s = socket

    def run(self):
        readbuffer = ''
        while True:
            readbuffer = readbuffer + self.s.recv(1024)
            temp = string.split(readbuffer, "\n")
            readbuffer = temp.pop()
            print(temp[0])

            for line in temp:
                # Checks whether the message is PING because its a method of Twitch to check if you're afk
                if (line[0] == "PING"):
                    self.s.send("PONG %s\r\n" % line[1])
                else:
                    # Splits the given string so we can work with it better
                    parts = string.split(line, ":")

                    if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                        try:
                            # Sets the message variable to the actual message sent
                            message = parts[2][:len(parts[2]) - 1]
                        except:
                            message = ""
                        # Sets the username variable to the actual username
                        usernamesplit = string.split(parts[1], "!")
                        username = usernamesplit[0]

