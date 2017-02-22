import random
import threading


class Stream(threading.Thread):
    name = ''
    interval = 10
    is_joined = False
    irc = None

    def __init__(self, name, event, irc, interval='10'):
        super(Stream, self).__init__()
        self.name = name
        self.interval = int(interval)
        self.stopped = event
        self.irc = irc
        self.start()

    def run(self):
        while not self.stopped.wait(self.getInterval):
            print 'trying to poyo'
            if not self.is_joined:
                self.irc.sendMessage('(> ^ - ^)> POYO <(^ - ^ <)', self.name)

    @property
    def getInterval(self):
        test = random.randint((self.interval * 60) - 90, (self.interval * 60) + 90)
        return test

    def getBaseInterval(self):
        return self.interval

    def setInterval(self, interval):
        self.interval = interval
