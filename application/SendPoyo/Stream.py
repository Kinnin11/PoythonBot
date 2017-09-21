import random
import threading


class Stream(threading.Thread):
    name = ''
    interval = 10
    is_joined = False
    irc = None
    quotes = True

    def __init__(self, name, event, irc, interval='10', quoteOption=True):
        super(Stream, self).__init__()
        self.name = name
        self.interval = int(interval)
        self.quotes = quoteOption
        self.stopped = event
        self.irc = irc
        self.start()


    def run(self):
        while not self.stopped.wait(self.getInterval):
            print 'trying to poyo in ' + self.name
            if self.is_joined:
                self.irc.sendMessage('(> ^ - ^)> POYO <(^ - ^ <)', self.name)

    @property
    def getInterval(self):
        test = random.randint((self.interval * 60) - 90, (self.interval * 60) + 90)
        return test

    def setQuoteOption(self, data):
        if data == '':
            if self.quotes:
                self.quotes = False
            else:
                self.quotes = True
        elif data == 'true':
            self.quotes = True
        elif data == 'on':
            self.quotes = True
        elif data == 'false':
            self.quotes = False
        elif data == 'off':
            self.quotes = False

    @property
    def getQuoteOption(self):
        return self.quotes

    def toString(self):
        return '{};{};{}'.format(self.name, self.interval, self.quotes)

    def getBaseInterval(self):
        return self.interval

    def setInterval(self, interval):
        self.interval = interval
