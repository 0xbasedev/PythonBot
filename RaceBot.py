import random
from Credentials import botowner, botname, botpassword
from SubspaceBot import *

class Rectangle:
	def __init__(self, ul_tile_x, ul_tile_y, lr_tile_x, lr_tile_y):
		self.ul_x = ul_tile_x * 16
		self.ul_y = ul_tile_y * 16
		self.lr_x = lr_tile_x * 16
		self.lr_y = lr_tile_y * 16
	
	def containsPlayer(self, player):
		# check if the player is inside the rectangle
		return True if player.x_pos >= self.ul_x and player.y_pos >= self.ul_y and player.x_pos < self.lr_x and player.y_pos < self.lr_y else False

class PlayerInfo:
	def __init__(self):
		self.start_ticks = None
		
if __name__ == '__main__':
	bot = SubspaceBot(botowner, 'This bot rolls a random number between 1 and 100')
	bot.connectToServer('66.235.184.102', 7900, botname, botpassword, '#python')
	
	print "Bot connected to server"
	
	beginning_warpto = (512, 512)
	start = Rectangle(478, 510, 483, 514)
	finish = Rectangle(541, 510, 545, 514)
	
	roll_start_id = bot.registerCommand('!race', 'Start the race')
	
	while bot.isConnected():
		event = bot.waitForEvent()
		if event.type == EVENT_ENTER:
			# initialize player info
			event.player.player_info = PlayerInfo()
		elif event.type == EVENT_POSITION_UPDATE:
			if event.player.player_info.start_ticks is None and start.containsPlayer(event.player):
				# the players start ticks is empty and hes entered the start area
				# start the race off and set his tick stamp
				event.player.player_info.start_ticks = GetTickCountHs()
				bot.sendArenaMessage('%s has started the race!' % event.player.name)
			if event.player.player_info.start_ticks is not None and finish.containsPlayer(event.player):
				# the player has a start tick stamp, and hes entered the finish area
				race_time = TickDiff(GetTickCountHs(), event.player.player_info.start_ticks) / 100.0
				bot.sendArenaMessage('%s finished the race in %f seconds!' % (event.player.name, race_time))
				# unset the tick stamp, so to start again he has to enter the start area
				event.player.player_info.start_ticks = None
		elif event.type == EVENT_COMMAND:
			if event.command.id == roll_start_id:
				bot.sendPrivateMessage(event.player, '*warpto %d %d' % beginning_warpto)
				bot.sendPrivateMessage(event.player, 'The race will start when you cross the start line')
				# unset his ticks, just in case he used the command from inside a race
				event.player.player_info.start_ticks = None
		
	print "Bot disconnected"
