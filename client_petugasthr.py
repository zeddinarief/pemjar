#import socket
import socket
import json
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim permintaan koneksi
sock.connect( ("127.0.0.1", 6667) )

data = {
    "command" : "PETUGAS",
}
datas = json.dumps(data)
sock.send(datas.encode('ascii'))

while True :
	msg = sock.recv(1000)
	msg = msg.decode('ascii')
	print(msg)