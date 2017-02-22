import threading

from application.Quotes.Quote import Quote
from application.SendPoyo.Stream import Stream


class DataService:
    @staticmethod
    def getStreams(irc):
        streams = open("..\streams.txt", "r")
        streamList = streams.readlines()
        output = []
        for s in streamList:
            split = s.split(';')
            output.append(Stream(split[0], threading.Event(), irc, interval=split[1]))
        streams.close()
        return output

    @staticmethod
    def getQuoteList():
        quotes = open("..\quotes.txt", 'r')
        quoteList = quotes.readlines()
        output = []
        for s in quoteList:
            output.append(Quote(s))
        return output

    @staticmethod
    def saveQuote(quote):
        quotes = open("..\quotes.txt", 'a+')
        quotes.write("\n" + quote)
        quotes.close()

    @staticmethod
    def getCommandList():
        commands = open("..\command.txt", 'r').readlines()
        output = []
        # for s in commands:

    @staticmethod
    def addStream(stream):
        streams = open("..\streams.txt", "a+")
        streams.write("\n" + stream.getName() + ";{}".format(stream.getBaseInterval()))
        streams.close()

    @staticmethod
    def deleteStream(user, streamList):
        streams = open("..\streams.txt", "w")
        for s in streamList:
            streams.write("{};{}".format(s.name, s.interval))

    @staticmethod
    def saveSuggestion(data):
        open("..\suggestion.txt", 'a+').write(data + "\n")
