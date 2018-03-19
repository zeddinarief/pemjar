#import socket
import socket
import struct
from fungsi1 import send_termination , recv_termination
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind addr
sock.bind( ('0.0.0.0', 6667) )

#listen sebanyak 100 permintaan
sock.listen(100)

while True:
	#menerima permintaan koneksi
	conn, client_addr = sock.accept()

	#terima string dari client
	data = recv_termination(conn)
	data = "20"+data
	
	print(data)
	
	#kirim balik respon
	send_termination(conn,data)
	#conn.send(data.encode('ascii'))
	#tutup koneksi
	conn.close()
