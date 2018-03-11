import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Kirim data ke server
data = "Selamat sore"
sock.sendto( data.encode('ascii'), ("192.168.100.255", 6666) )
# Baca dari server
server_data, server_addr = sock.recvfrom(1000)
# Cetak ke layar
print(server_data.decode('ascii'))