from scapy.all import *

minport = 77
maxport = 81
list_port = []
for numport in range(minport,maxport):
	
	tcp_packet = IP(src="192.168.100.7",dst="175.45.187.242")/TCP(sport=7778,dport=numport,flags="S")
	reply = sr1(tcp_packet,timeout = 3)
	try:
		flag = reply.getlayer(TCP).flags
		print(flag)
		if(flag == "SA"):
			#print(reply)
			port = "port "+str(numport)+" open"
			print("The port "+ str(numport) +" is open")
			list_port.append(port)
	except:
		port = "port "+str(numport)+" close"
		print("The port "+ str(numport) +" is Closed")
		list_port.append(port)
	
print("Daftar port")
print(list_port)