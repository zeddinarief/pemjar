import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("when: ")
sock.sendto(msg.encode('ascii'), ("127.0.0.1",6667) )
#pakai recv saja boleh recvfrom boleh karene sudah tahu alamat yang dituju
data = sock.recv(1000)

print(data.decode('ascii'))