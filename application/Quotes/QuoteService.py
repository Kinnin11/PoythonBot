import random

from data.DataService import DataService


class QuoteService:
    quotesList = DataService.getQuoteList()

    def getQuote(self):
        counter = 0
        while counter < len(self.quotesList):
            counter += 1
            rand = random.randint(0, len(self.quotesList) - 1)
            out = self.quotesList[rand].getQuote()
            if out is not None:
                return out

        rand = random.randint(0, len(self.quotesList) - 1)
        return self.quotesList[rand].content
