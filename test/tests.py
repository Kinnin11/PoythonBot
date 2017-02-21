from application.IRC.IRCHandler import IRCHandler

from application.Quotes.QuoteService import QuoteService

irc = IRCHandler()
quotes = QuoteService()
irc.sendMessage(quotes.getQuote(), "#poyobot")
