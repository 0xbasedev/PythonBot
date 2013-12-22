#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *


if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot announces ship changes')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_CHANGE:
			if event.old_ship != event.player.ship:
				bot.sendArenaMessage(event.player.name + ' changed from ' + GetShipName(event.old_ship) + ' to ' + GetShipName(event.player.ship) + '!')
			
	print "Bot disconnected"
