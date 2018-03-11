import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("when: ")
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(msg.encode('ascii'), ("127.255.255.255",6667) )
#pakai recv saja boleh recvfrom boleh karene sudah tahu alamat yang dituju

while True:
		
	data, addr = sock.recvfrom(1000)

	print(data.decode('ascii'))

