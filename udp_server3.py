#import socket
import socket
from datetime import date,timedelta
#inisialisasi socket
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

#bind ip dan port tertentu 
sock.bind( ("127.100.2.25",6665) )

while True: 	
	#baca data dari client
	data, client_address = sock.recvfrom(1000)
	data = data.decode('ascii')
	#ubah data dan kirim
	if data == "yesterday":
		now = "server3 : "+str(date.today()+timedelta(-1))
		sock.sendto(now.encode('ascii'), client_address)
	elif data == "today":
		now = "server3 : "+str(date.today())
		sock.sendto(now.encode('ascii'), client_address)
	elif data == "tomorrow":
		now = "server3 : "+str(date.today()+timedelta(+1))
		sock.sendto(now.encode('ascii'), client_address)
	else:
		now = "server3 : "+"no date"
		sock.sendto(now.encode('ascii'), client_address)
	#data = "OK " +data.decode('ascii')
	#sock.sendto(data.encode('ascii'), client_address)
	