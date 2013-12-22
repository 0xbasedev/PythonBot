#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *

class PlayerInfo():
	def __init__(self):
		self.consecutive_kills = 0

if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot announces kill sprees to the arena')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_ENTER:
			event.player.player_info = PlayerInfo()
		if event.type == EVENT_KILL:
			# increment the killers consecutive kills and announce if its time
			p = event.killer
			pi = event.killer.player_info
			pi.consecutive_kills += 1
			if pi.consecutive_kills >= 5 and pi.consecutive_kills % 5 == 0:
				bot.sendArenaMessage(event.killer.name + ' is on a spree with ' + str(pi.consecutive_kills) + ' kills!')
			
			# announce the end of a kill-streak if the player has one, then reset the killed players consecutive kill count
			p = event.killed
			pi = event.killed.player_info
			if pi.consecutive_kills >= 5:
				bot.sendArenaMessage(p.name + '\'s ' + str(pi.consecutive_kills) + '-kill streak was ended by ' + event.killer.name + '!')
			pi.consecutive_kills = 0
		
	print "Bot disconnected"
