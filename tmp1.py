#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  безіменний.py
#  
#  Copyright 2013  <way01@i7way>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



#import getpass
#import sys
#import telnetlib

#HOST = "localhost"
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

#tn = telnetlib.Telnet(HOST)

#tn.read_until("login: ")
#tn.write(user + "\n")
#if password:
    #tn.read_until("Password: ")
    #tn.write(password + "\n")

#tn.write("ls\n")
#tn.write("exit\n")

#print tn.read_all()

import getpass
import sys
import telnetlib

#http://developer.android.com/tools/devices/emulator.html#netspeed
def main():
	HOST = "localhost"
	user = raw_input("Enter your remote account: ")
	password = getpass.getpass()

	tn = telnetlib.Telnet("localhost", 5554)
	#tn.interact()
	#tn.read_until("login: ")
	#tn.write(user + "\n")
	#if password:
	#	tn.read_until("Password: ")
	#	tn.write(password + "\n")

	#tn.write("ls\n")
	#tn.write("exit\n")
	#tn.read_until("account: ")
	#tn.write("\r")
	#tn.write("help\n")
	#status           dump network status
    #speed            change network speed
    #delay            change network latency
    #capture      
    
	tn.write("network status\n")
	
	
	#tn.write("network speed gsm\n")
	tn.write("network speed full\n")
	#tn.write("network delay gprs\n")
	tn.write("network delay none\n")
	tn.write("network status\n")
	tn.write("exit\n")
	
	print tn.read_all()
	
	return 0

if __name__ == '__main__':
	main()

