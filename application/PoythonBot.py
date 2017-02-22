from application.IRC.IRCHandler import IRCHandler
from data.DataService import DataService

irc = IRCHandler()

streamList = DataService.getStreams(irc)
