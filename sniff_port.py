from scapy.all import *

def packet(packet):
    if IP in packet:
        ip_src=packet[IP].src
        ip_dst=packet[IP].dst
    if TCP in packet:
        tcp_sport=packet[TCP].sport
        tcp_dport=packet[TCP].dport

        print " IP src " + str(ip_src) + " TCP sport " + str(tcp_sport) 
        print " IP dst " + str(ip_dst) + " TCP dport " + str(tcp_dport)
    
packets=sniff(filter="ip", prn=packet)