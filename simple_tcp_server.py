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
	'''
	# [::-1] reverse word
	data = "OK "+data[::-1]

	data = int(data)
	if data%2==1:
		data = "ganjil"
	else :
		data = "genap"
	'''
		
	#kirim balik respon
	conn.send(respon.encode('ascii'))
	#conn.send(data.encode('ascii'))
	#tutup koneksi
	conn.close()
