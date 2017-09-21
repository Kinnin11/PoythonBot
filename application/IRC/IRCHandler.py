import socket
import threading

from application.IRC import IRCThread
from application.Quotes.QuoteService import QuoteService
from application.SendPoyo.StreamChecker import StreamChecker


class IRCHandler:
    s = socket.socket()
    thread = None
    thread2 = None
    streamList = None
    quoteService = QuoteService()

    def __init__(self):
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

        # Loading the list of streams to check
        from data.DataService import DataService
        self.streamList = DataService.getStreams(self)

        # starting the IRC reader and StreamliveChecker
        self.thread = IRCThread.IRCThread(self.s, self)
        self.thread.start()
        self.thread2 = StreamChecker(self.s, self, threading.Event())
        self.thread2.start()

    #useful commands for interacting with IRC
    def refreshQuotes(self):
        self.thread2 = StreamChecker(self.s, self, threading.Event())
        self.thread2.start()

    def sendMessage(self, message, channel):
        self.s.send("PRIVMSG " + channel + " :" + message + "\r\n")
        print ("PRIVMSG " + channel + " :" + message)

    def handleJoin(self, channel):
        self.s.send("JOIN " + channel + "\r\n")
        print("joining channel: " + channel)

    def handlePart(self, channel):
        self.s.send("PART " + channel + "\r\n")
        print("leaving channel: " + channel)
