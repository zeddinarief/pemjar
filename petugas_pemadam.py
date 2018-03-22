#import socket
import socket
import json
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )
while True:
    
    print("selamat bekerja")
    nama = "petugas,"
    sock.send(nama.encode('ascii'))
    #baca respon dari server
    data = sock.recv(100)
    data = data.decode('ascii')
    if data:
        print("laporan kebakaran dari : "+data)

