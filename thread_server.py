#import socket
import socket
#import select
import threading

#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind addr
sock.bind( ('0.0.0.0', 6667) )

#listen sebanyak 100 permintaan
sock.listen(100)
#list_monitor = [ sock ]
def handle_thread(conn):
    while True:
        try:
            #terima string dari client
            data = conn.recv(100)
            data = data.decode('ascii')
        	# [::-1] reverse word
            data = "OK "+data[::-1]
        	#kirim balik respon
            conn.send(data.encode('ascii'))
        	#conn.send(data.encode('ascii'))
        except(socket.error):
        	#tutup koneksi
            break
        	#conn.close()

while True:
	#menerima permintaan koneksi
    conn, client_addr = sock.accept()
    buat thread baru untuk setiap permintaan koneksi
    t = threading.Thread(target=handle_thread, args=(conn,))
    start thread
    t.start()
