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
            datasp = data.split()
            if data == "exit":
                #tutup koneksi
                print("koneksi dituup")
                break
            else:    
                if datasp[0] == "new":
                    files = open(datasp[1],"w")
                    res = data.split(datasp[1]+" ")
                    files.write(res[1])
                    respon = "OK"
                    files.close()
                elif datasp[0] == "read":
                    files = open(datasp[1],"r")
                    respon = files.read()
                    files.close()
                elif datasp[0] == "del":
                    os.remove(datasp[1])
                    respon = "OK"
                else:
                    respon = "perintah tidak ditemukan"

                #kirim balik respon
                conn.send(respon.encode('ascii'))
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
