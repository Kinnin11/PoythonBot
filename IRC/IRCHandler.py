import socket, string
import threading

from IRC import IRCThread

#connects to IRC and starts up the chatreader, also has useful commands
class IRCHandler:
    def __init__(self):
        pass

    HOST = "irc.twitch.tv"
    NICK = "poyobot"
    PORT = 6667
    PASS = "oauth:fqvokjqzezh8nl9b03334tf13gp6lm"
    MODT = False


    # Connecting to Twitch IRC by passing credentials and joining a certain channel
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + NICK + "\r\n")
    s.send("JOIN #poyobot \r\n")

    thread = IRCThread.IRCThread(s)
    thread.start()

    def sendMessage(self, message, channel):
        self.s.send("PRIVMSG " + channel + " :" + message + "\r\n")
        print ("PRIVMSG " + channel + " :" + message + "\r\n")

    def handleJoin(self,channel):
        self.s.send("JOIN " + channel + "\r\n")
        print("joining channel: " + channel)

    def handlePart(self, channel):
        self.s.send("PART " + channel + "\r\n")
        print("leaving channel: " + channel)


