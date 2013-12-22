#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *


if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot changes ship and freq')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	ship_command_id = bot.registerCommand('!ship', 'Change ship')
	freq_command_id = bot.registerCommand('!freq', 'Change ship')
	setposition_command_id = bot.registerCommand('!setposition', 'Change position')
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_COMMAND:
			if event.command.id == ship_command_id:
				if len(event.arguments) == 1:
					bot.requestShipChange(int(event.arguments[0]))
			elif event.command.id == freq_command_id:
				if len(event.arguments) == 1:
					bot.requestFreqChange(int(event.arguments[0]))
			elif event.command.id == setposition_command_id:
				if len(event.arguments) == 4:
					bot.setPosition(int(event.arguments[0]), int(event.arguments[1]), int(event.arguments[2]), int(event.arguments[3]))
		
	print "Bot disconnected"
