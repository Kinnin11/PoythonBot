from datetime import datetime, timedelta

from application.Commands.UserLevel import UserLevel


class Command:
    respondTo = ''
    respondWith = ''
    cooldown = 20
    activeCooldowns = {}
    userlevel = UserLevel.Viewer

    def __init__(self, respondTo, respondWith='', userlevel=UserLevel.Viewer, cooldown=20):
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
        if user != 'kinnin11':
            if self.checks(user, stream):
                self.activeCooldowns[stream] = datetime.now() + timedelta(self.cooldown)
                return True
            else:
                return False
        return True
