from application.Commands.AddQuoteCommand import AddQuoteCommand
from application.Commands.CheckInterval import CheckInterval
from application.Commands.PoyoCommand import PoyoCommand
from application.Commands.QuoteCommand import QuoteCommand
from application.Commands.QuoteOptionCommand import QuoteOptionCommand
from application.Commands.RefreshQuotesCommand import RefreshQuotesCommand
from application.Commands.RegisterCommand import RegisterCommand
from application.Commands.SetIntervalCommand import SetIntervalCommand
from application.Commands.SuggestQuoteCommand import SuggestQuoteCommand
from application.Commands.UnregisterCommand import UnregisterCommand
from application.Commands.UserLevel import UserLevel
from application.Commands.VariableMSGCommand import VariableMSGCommand


class CommandBuilder:
    def buildCommand(self, commandType, respondTo, respondWith='', userlevel="V", cooldown=20):
        commandLevel = None
        if userlevel == "V":
            commandLevel = UserLevel.Viewer
        elif userlevel == "M":
            commandLevel = UserLevel.Mod
        elif userlevel == "S":
            commandLevel = UserLevel.Streamer
        elif userlevel == "K":
            commandLevel = UserLevel.Kinnin11

        if commandType == 'AQ':
            return AddQuoteCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'CI':
            return CheckInterval(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'P':
            return PoyoCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'QO':
            return QuoteOptionCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'RQ':
            return RefreshQuotesCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'R':
            return RegisterCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'SI':
            return SetIntervalCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'SQ':
            return SuggestQuoteCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'U':
            return UnregisterCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'VMSG':
            return VariableMSGCommand(respondTo, respondWith, commandLevel, cooldown)
        elif commandType == 'Q':
            return QuoteCommand(respondTo, respondWith, commandLevel, cooldown)
