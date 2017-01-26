import socket, string
import threading

from IRC import IRCThread


# connects to IRC and starts up the chatreader, also has useful commands
from SendPoyo.StreamChecker import StreamChecker


class IRCHandler:

    s = socket.socket()

    def __init__(self):
        pass
        HOST = "irc.twitch.tv"
        NICK = "poyobot"
        PORT = 6667
        PASS = "oauth:fqvokjqzezh8nl9b03334tf13gp6lm"
        MODT = False

        # Connecting to Twitch IRC by passing credentials and joining the poyobot channel
        self.s.connect((HOST, PORT))
        self.s.send("PASS " + PASS + "\r\n")
        self.s.send("NICK " + NICK + "\r\n")
        self.s.send("JOIN #poyobot \r\n")

        thread = IRCThread.IRCThread(self.s)
        thread.start()
        thread2 = StreamChecker(self.s, self, threading.Event())
        thread2.start()

    def sendMessage(self, message, channel):
        self.s.send("PRIVMSG " + channel + " :" + message + "\r\n")
        print ("PRIVMSG " + channel + " :" + message + "\r\n")

    def handleJoin(self, channel):
        self.s.send("JOIN " + channel + "\r\n")
        print("joining channel: " + channel)

    def handlePart(self, channel):
        self.s.send("PART " + channel + "\r\n")
        print("leaving channel: " + channel)
