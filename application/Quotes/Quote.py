from datetime import datetime, timedelta


class Quote:
    content = ''
    lastUsed = datetime.now()

    def __init__(self, concent):
        self.content = concent
        print self.lastUsed
        self.lastUsed -= timedelta(0, 3600)
        print self.lastUsed

    def getQuote(self):
        if self.lastUsed >= datetime.now():
            return self.content
        else:
            return None
