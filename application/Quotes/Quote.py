from datetime import datetime, timedelta


class Quote:
    content = ''
    lastUsed = datetime.now()

    def __init__(self, content):
        self.content = content
        self.lastUsed -= timedelta(0, 3600)

    def getQuote(self):
        if self.lastUsed <= datetime.now():
            self.lastUsed = datetime.now() + timedelta(0, 3600)
            return self.content.strip('\n')
        else:
            return None
