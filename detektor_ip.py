from scapy.all import *
import time
def tcp_packet(packet):
    if IP in packet:
    	start_time = time.time()
        size = packet.len    
        time = (time.time() - start_time)

        if time > 60 :
            print("Terdapat sebuah serangan IP flood dari IP " + packet.getlayer(IP).src)

pkts=sniff(filter="tcp", prn=tcp_packet)