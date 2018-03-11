#Import lib socket
import socket

# Inisiasi objek socket UDP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Ikat ke IP dan port tertentu
sock.bind( ("0.0.0.0", 6666) )

while True :
    # Baca data yang diterima dari client
    data, client_address = sock.recvfrom(1000)
    print(data)
    # Ubah data
    data = "OK "+data.decode('ascii')
    # Kirim balik ke client
    sock.sendto( data.encode('ascii'), client_address )
