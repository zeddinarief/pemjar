#import socket
import socket
import struct
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )

#kirim data
data = 50000000
# representasi variabel data sebagai unsign little endian membaca bit dari kiri
sock.send(struct.pack("<I",data))

#baca respon dari server
data = sock.recv(100)
data = struct.unpack("<I", data)[0]
print(data)

#tutup koneksi
sock.close()
