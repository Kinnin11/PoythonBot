import threading

import schedule as schedule

import twitch


class StreamChecker(threading.Thread):
    def run(self):
        schedule.every(10).minutes.do(self.checkStreams())

    def checkStreams(self):
        twitch.streams.by_channel()
