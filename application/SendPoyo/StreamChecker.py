import threading

import twitch.api.v3 as twitch
from data.DataService import DataService


class StreamChecker(threading.Thread):
    streamList = None
    handler = None

    def __init__(self, socket, irc, event):
        super(StreamChecker, self).__init__()
        self.s = socket
        self.handler = irc
        self.stopped = event
        self.streamList = DataService.getStreams(irc)

    def run(self):
        print('starting to check if streams are live')
        self.checkStreams()
        while not self.stopped.wait(60):
            self.checkStreams()

    def checkStreams(self):
        for stream in self.streamList:
            print('checking stream ' + stream.name)
            if twitch.streams.by_channel(stream.name[1:]).get('stream') is not None and not stream.is_joined:
                self.handler.handleJoin(stream.name)
                stream.is_joined = True
            elif twitch.streams.by_channel(stream.name[1:]).get('stream') is None and stream.is_joined:
                self.handler.handlePart(stream.name)
                stream.is_joined = False
            print ('stream {} is {}'.format(stream.name, stream.is_joined))
