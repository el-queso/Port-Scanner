#!/bin/python
# A shitty port scanner! 

#Imports
import sys
import socket
from datetime import datetime

#Define the target!
if len(sys.argv) == 2: 
	target = socket.gethostbyname(sys.argv[1]) #Translating hostname to IPv4!!
else: 
	print("Invalid ammount of arguments.")
	print("Syntax: python3 scanner.py <IP>")
#############################################
#Adding a banner
print("#" * 50)
print ("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("#" * 50)
#############################################
try:
	for port in range(50,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # S= wanna connect to IPv4 and determine the port
		socket.setdefaulttimeout(1) # Attempt to connect to a port and if not connected w8 for only 1 sec!
		result = s.connect_ex((target,port)) #return an error indicator
		#print ("Checking port {}".format(port)) #Checking The port status!		
		if result == 0: # OPEN PORT!
			print ("Port {} is open".format(port))
			print("-" * 50)		
		s.close()

#Exceptions
except KeyboardInterrupt:
	print ("\nEnan logo pou pathses ^C...")
	sys.exit()

except socket.gaierror:
	print ("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
