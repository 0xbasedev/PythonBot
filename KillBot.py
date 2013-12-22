#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *


if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot announces kills to the arena')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_KILL:
			bot.sendArenaMessage(event.killer.name + ' killed ' + event.killed.name + '!')
		
	print "Bot disconnected"
