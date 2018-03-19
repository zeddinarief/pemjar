#import socket
import socket
import struct
from fungsi1 import send_size , recv_size
#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind addr
sock.bind( ('0.0.0.0', 6667) )

#listen sebanyak 100 permintaan
sock.listen(100)

while True :
    # Terima permintaan koneksi
    conn, client_address = sock.accept()
    # Terima string dari client
    data = recv_size(conn)
    # Tambah "OK"
    data = "OK "+data
    # Kirim balik ke client
    send_size(conn, data)
    # Tutup koneksi
    #conn.close()
