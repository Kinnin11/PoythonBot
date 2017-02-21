import socket
import threading

from application.IRC import IRCThread
from application.SendPoyo.StreamChecker import StreamChecker


class IRCHandler:
    s = socket.socket()
    thread = None

    def __init__(self):
        pass
        HOST = "irc.twitch.tv"
        NICK = "poyobot"
        PORT = 6667
        PASS = open("..\password.txt").read()
        MODT = False

        # Connecting to Twitch IRC by passing credentials and joining the poyobot channel
        self.s.connect((HOST, PORT))
        self.s.send("PASS " + PASS + "\r\n")
        self.s.send("NICK " + NICK + "\r\n")
        self.s.send("JOIN #poyobot \r\n")

        self.thread = IRCThread.IRCThread(self.s)
        self.thread.start()
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
