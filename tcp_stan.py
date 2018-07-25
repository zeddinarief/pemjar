#! /usr/bin/python3

from scapy.all import *
import sys

ip = input("Masukkan IP tujuan : ")

SYNACK = 0x12
RSTACK = 0x14


#Fungsi scan
def port_scan(port):
	srcport = 7778
	conf.verb = 0
	SYNACKpacket = sr1(IP(dst = ip)/TCP(sport = srcport, dport = port, flags = "S"),timeout = 3)
	try:
		flagpacket = SYNACKpacket.getlayer(TCP).flags
		if flagpacket == SYNACK:
			return True
		else:
			return False
		close = IP(dst = ip)/TCP(sport = srcport, dport = port, flags = "R")
		send(close)
	except:
		return False

for port in range(10,21):
	status = port_scan(port)
	if status == True:
		print("Port " + str(port) + " terbuka")
	else:
		print("Port " + str(port) + " tertutup")