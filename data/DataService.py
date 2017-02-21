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
            output.append(Stream(split[0], split[1], threading.Event(), irc))
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
