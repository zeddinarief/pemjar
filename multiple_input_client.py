#import socket
import socket

#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )

#kirim data
data = "hai"
sock.send(data.encode('ascii'))

#baca respon dari server
data = sock.recv(100)
data = data.decode('ascii')
print(data)

#kirim data
data = "hai kaka"
sock.send(data.encode('ascii'))

#baca respon dari server
data = sock.recv(100)
data = data.decode('ascii')
print(data)

#tutup koneksi
#sock.close()
