#!/usr/bin/env python

import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *


if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot sets timers')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	timer_command_id = bot.registerCommand('!timer', 'Set a timer')
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_COMMAND:
			if event.command.id == timer_command_id:
				if len(event.arguments) == 1:
					bot.setTimer(int(event.arguments[0]), event.player.name)
					bot.sendPrivateMessage(event.player.name, "Ok")
				else:
					bot.sendPrivateMessage(event.player.name, "Usage: !timer <seconds>")
		elif event.type == EVENT_TIMER:
			bot.sendPrivateMessage(event.user_data, "Timer expired")
		
	print "Bot disconnected"
