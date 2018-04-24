from scapy.all import *

tcp_packet = IP(src="10.34.220.71" , dst="175.45.187.242")/TCP(sport=7778,dport=80)

reply = sr1(tcp_packet)
reply.show()