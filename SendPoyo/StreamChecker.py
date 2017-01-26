import threading
import twitch.api.v3 as twitch
import six

from SendPoyo.Stream import Stream


class StreamChecker(threading.Thread):

    handler = None

    stream = Stream('#krepo', 10)

    def __init__(self, socket,irc, event):
        super(StreamChecker, self).__init__()
        self.s = socket
        self.handler = irc
        self.stopped = event

    def run(self):
        print('starting to check if streams are live')
        while not self.stopped.wait(60):
            self.checkStreams()

    def checkStreams(self):
        by_name = twitch.streams.by_channel('krepo').get('stream')
        print('checking stream ' + self.stream.name)
        if twitch.streams.by_channel(self.stream.name[1:]).get('stream') is not None and self.stream.is_joined is False:
            self.handler.handleJoin(self.stream.name)
            self.stream.is_joined = True

