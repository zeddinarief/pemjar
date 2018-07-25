#import socket
import socket,os

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
	data = conn.recv(100)
	data = data.decode('ascii')
	respon = "ok"
	print(data)
	conn.send(respon.encode('ascii'))
	conn.close()
