from scapy.all import *
import socket

SYN = 0x02

conf.verb = 0
# Fungsi untuk handle packet masuk
def handle_packet(packet):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        if packet[TCP].flags & SYN : 
            send(IP(dst=packet[IP].src, src=packet[IP].dst)/TCP(dport=packet[IP].sport, sport=packet[IP].dport,
                                          ack=packet[IP].seq + 1, flags='SA'))
            print("Paket dari IP "+src_ip+" ke "+dst_ip+" src_port "+str(src_port)+" d_port"+str(dst_port))
        else :
            pass
    else :
        print("Bukan paket TCP")
    
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.connect( ("192.168.43.203", 6667) )
    data = ""+str(src_ip)
    tcp_sock.send( data.encode('ascii') )
    data = tcp_sock.recv(100)
    data = data.decode('ascii')
    tcp_sock.close()


sniff(iface="wlp3s0", filter="tcp and portrange 10-20", prn=handle_packet)
