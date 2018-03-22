#import socket
import socket
import json
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )
while True:
	
	#kirim data
	print("menu :")
	print("1. memberi laporan")
	print("2. exit")
	menu = input("pilih menu no : ")

	if menu == "2":
		#tutup koneksi
		sock.send(data.encode('ascii'))
		sock.close()
		break
	elif menu == "1":
		print("format : nama,alamat")
		data = input("--> ")
		#laporan = {"nama" : nama , "alamat" : alamat}
		sock.send(data.encode('ascii'))

		#baca respon dari server
		data = sock.recv(100)
		data = data.decode('ascii')
		print(data)
	else:
		print("menu tidak tersedia")
		sock.close()
		break
