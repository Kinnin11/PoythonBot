from datetime import datetime


class UserLevel:
    Kinnin11, Streamer, Mod, Viewer = range(4)


class Command:
    respondTo = ''
    respondWith = ''
    cooldown = 20
    activeCooldowns = {}
    userlevel = UserLevel.Viewer

    def __init__(self, respondTo, respondWith, userlevel, cooldown=20):
        self.respondTo = respondTo
        self.respondWith = respondWith
        self.cooldown = cooldown
        self.userlevel = userlevel

    def checkCooldown(self, stream):
        if stream in self.activeCooldowns:
            return self.activeCooldowns.get(stream) <= datetime.now()
        return True

    def checkUserLevel(self, user, stream):
        if self.userlevel == UserLevel.Viewer:
            return True
        if self.userlevel == UserLevel.Mod:
            return True
        if self.userlevel == UserLevel.Streamer:
            return user == stream[1:]
        if self.userlevel == UserLevel.Kinnin11:
            return user == "kinnin11"

    def checks(self, user, stream):
        return self.checkCooldown(stream) & self.checkUserLevel(user, stream)

    def handle(self, user, stream, data, irc):
        if self.checks(user, stream):
            self.activeCooldowns[stream] = datetime.now() + datetime.timedelta(self.cooldown)
            return True
