#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *


if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot gives you an arena list')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	arena_command_id = bot.registerCommand('!arena', 'List the arenas in the zone')
	requester_names = []
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_COMMAND:
			if event.command.id == arena_command_id:
				requester_names.append(event.player.name)
				bot.sendPublicMessage("?arena")
		elif event.type == EVENT_ARENA_LIST:
			if len(requester_names) > 0:
				player_name = requester_names.pop(0)
				for arena_name, num_players in event.arena_list:
					bot.sendPrivateMessage(player_name, 'Arena: %s - %d' % (arena_name, num_players))
		
	print "Bot disconnected"
