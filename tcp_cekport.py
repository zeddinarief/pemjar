from scapy.all import *

srcip = "10.113.1.71"
dstip = "180.250.177.10"
'''
minport = input("port minimal = ")
maxport = input("port maksimal = ")
'''
minport = "85"
maxport = "90"
list_port = []
for numport in range(int(minport),int(maxport)):
	
	tcp_packet = IP(src=srcip, dst=dstip)/TCP(sport=7778,dport=numport,flags="S")
	reply = sr1(tcp_packet,timeout = 2)
	try:
		flag = reply.getlayer(TCP).flags
		print(flag)
		'''
		if(flag == "SA"):
			port = "port "+str(numport)+" open"
			print("The port "+ str(numport) +" is open")
			list_port.append(port)
			'''
		if(flag):
			if(flag == "SA"):
				port = "port "+str(numport)+" open"
				print("The port "+ str(numport) +" is open")
				list_port.append(port)
			else:
				print("The port "+ str(numport) +" is close")
	except:
		port = "port "+str(numport)+" close"
		print("The port "+ str(numport) +" is Closed")
		list_port.append(port)
	
print("Daftar port")
print(list_port)