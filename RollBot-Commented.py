#!/usr/bin/env python

# import python's random library for the random.randrange() function
import random

# import our credentials from file. this prevents us from embedding our
# username/password in our bot files
from Credentials import botowner, botname, botpassword

# import the SubspaceBot class. this is what has all the features we need
from SubspaceBot import *


if __name__ == '__main__':
	# initialize the bot, setting its owner and description, then connecting to the server
	bot = SubspaceBot(botowner, 'This bot rolls a random number between 1 and 100')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	# register two commands, !roll and !about
	roll_command_id = bot.registerCommand('!roll', 'Roll a number between 1 and 100')
	
	# keep looping as long as the bot is connected. at each loop, pull out the next
	# even that is waiting for us to process
	while bot.isConnected():
		event = bot.waitForEvent()
		
		# based on the event type, 
		if event.type == EVENT_COMMAND:
			# based on what type of command this is, handle it accordingly
			if event.command.id == roll_command_id:
				# this command is the !roll command
				random_number = random.randrange(1, 101)
				bot.sendArenaMessage(event.player.name + ' rolled ' + str(random_number) + ' (1-100)')
		
	print "Bot disconnected"
