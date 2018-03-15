#import socket
import socket

#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )
while True:
	
	#kirim data
	print("format : \nnew namafile.txt isi \nread namafile.txt \ndel namafile.txt \nexit")

	data = input("--> ")

	if data == "exit":
		#tutup koneksi
		sock.send(data.encode('ascii'))
		sock.close()
		break
	else:

		sock.send(data.encode('ascii'))

		#baca respon dari server
		data = sock.recv(100)
		data = data.decode('ascii')
		print(data)

