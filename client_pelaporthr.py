#import socket
import socket
import json
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )

alamat = input("masukkan alamat : ")
data = {
    "command" : "LAPOR",
    "alamat" : alamat
}
datas = json.dumps(data)
sock.send(datas.encode('ascii'))

reply = sock.recv(1000)
reply = reply.decode('ascii')
print(reply)

