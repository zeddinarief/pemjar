#import socket
import socket,os
import struct
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
	data = conn.recv(4)
	data = struct.unpack("<I", data)[0]

	data = 20+data
	
	print(data)
	#kirim balik respon
	conn.send(struct.pack("<I", data))
	#conn.send(data.encode('ascii'))
	#tutup koneksi
	conn.close()
