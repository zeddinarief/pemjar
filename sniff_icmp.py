from scapy.all import *

def icmp_packet(packet):
    if IP in packet:
        size = packet.len    
        if size > 50000 :
            print("Terdapat sebuah serangan ICMP flood dari IP " + packet.getlayer(IP).src)
            
        if packet[IP].dst == "192.168.137.192" :
            print("ip from "+packet[IP].src)

pkts=sniff(filter="icmp", prn=icmp_packet)