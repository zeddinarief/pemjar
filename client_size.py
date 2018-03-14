#import socket
import socket
import struct
from fungsi1 import send_size , recv_size
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )

#kirim data
data = "jurusan teknik informatika "
send_size(sock,data)

#baca respon dari server
data = recv_size(sock)
data = data.decode('ascii')
print(data)

#tutup koneksi
sock.close()
