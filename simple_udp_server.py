#import socket
import socket
from datetime import date,timedelta
#inisialisasi socket
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

#bind ip dan port tertentu 
sock.bind( ("0.0.0.0",6667) )

#baca data dari client
data, client_address = sock.recvfrom(1000)
data = data.decode('ascii')
data = "OK "+data

sock.sendto(data.encode('ascii'), client_address)
'''
while True: 	
	#baca data dari client
	data, client_address = sock.recvfrom(1000)
	data = data.decode('ascii')
	#ubah data dan kirim
	if data == "yesterday":
		now = str(date.today()+timedelta(-1))
		sock.sendto(now.encode('ascii'), client_address)
	elif data == "today":
		now = str(date.today())
		sock.sendto(now.encode('ascii'), client_address)
	elif data == "tomorrow":
		now = str(date.today()+timedelta(+1))
		sock.sendto(now.encode('ascii'), client_address)
	else:
		now = "no date"
		sock.sendto(now.encode('ascii'), client_address)
	#data = "OK " +data.decode('ascii')
	#sock.sendto(data.encode('ascii'), client_address)
'''