#import socket
import socket
#import select
import threading
import json

#inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind addr
sock.bind( ('0.0.0.0', 6667) )

#listen sebanyak 100 permintaan
sock.listen(100)

'''
#format untuk lapor
{
    "command" : LAPOR
}

{
    "command" : PETUGAS
}
'''

list_petugas = []
def handle_thread(conn):
    while True:
        try:
            #terima string dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            data = json.loads(data)
            msg = ""
        	# [::-1] reverse word
            if data["command"] == "LAPOR":
                for c in list_petugas :
                    alamat = data["alamat"]
                    msg = "laporan terkirim !"
            	    #kirim balik respon
                    c.send(alamat.encode('ascii'))
            elif data["command"] == "PETUGAS":
                msg = "Petugas berhasil terdaftar"
                list_petugas.append(conn)
            else:                
                msg = "Command tidak tersedia"
            conn.send(msg.encode('ascii'))
        except(socket.error):
        	#tutup koneksi
            print("koneksi ditutup")
            break
            #conn.close()
            

while True:
	#menerima permintaan koneksi
    conn, client_addr = sock.accept()
    #buat thread baru untuk setiap permintaan koneksi
    t = threading.Thread(target=handle_thread, args=(conn,))
    #start thread
    t.start()
