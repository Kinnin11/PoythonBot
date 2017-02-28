# from application.Commands import *

from data.DataService import DataService

print globals().keys()

DataService().loadCommands()
