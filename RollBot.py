#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *


if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot rolls a random number between 1 and 100')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	roll_command_id = bot.registerCommand('!roll', 'Roll a number between 1 and 100')
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_COMMAND:
			if event.command.id == roll_command_id:
				random_number = random.randrange(1, 101)
				bot.sendArenaMessage(event.player.name + ' rolled ' + str(random_number) + ' (1-100)')
		
	print "Bot disconnected"
