from application.Quotes.Quote import Quote
from application.SendPoyo.Stream import Stream


class DataService:
    def getStreams(self):
        streams = open("..\streams.txt", "r")
        streamList = streams.readlines()
        output = []
        for s in streamList:
            split = s.split(';')
            output.append(Stream(split[0], split[1]))
        streams.close()
        return output

    def getQuoteList(self):
        quotes = open("..\quotes.txt", 'r')
        quoteList = quotes.readlines()
        output = []
        for s in quoteList:
            output.append(Quote(s))
        return output

    def saveQuote(self, quote):
        quotes = open("..\quotes.txt", 'a+')
        quotes.write("\n" + quote)
        quotes.close()
