#!/usr/bin/env python

#
# This file needs to be named 'Credentials.py'
#

botowner = None		# change to 'your_user_name' including quotes
botpassword = None	# change to 'your_bots_password' including quotes
botname = None		# change to 'your_bots_name' including quotes

if botowner is None or botpassword is None or botname is None:
	raise 'Values for botowner, botpassword, and botname must all be set in Credentials.py!'
