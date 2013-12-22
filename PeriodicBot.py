#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *


if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot announces an arena message periodically')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	last_arena_ticks = GetTickCountHs()
	interval = 5 * 60 * 100	# 5 minutes * 60 -> seconds, seconds * 100 -> hundreths of seconds
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_TICK:
			if (GetTickCountHs() - last_arena_ticks) & 0xFFFFFFFF >= interval:
				bot.sendArenaMessage('5 minutes have passed since the last message')
				last_arena_ticks = GetTickCountHs()
			
	print "Bot disconnected"
