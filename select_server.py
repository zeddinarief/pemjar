# Import socket
import socket
import select

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke address dan port tertentu
sock.bind( ('0.0.0.0', 6667) )

# Listen sebanyak 100 permintaan koneksi
sock.listen(100)

list_monitor = [ sock ]

laporan = []
while True :

    inputready, outputready, errorready = select.select(list_monitor, [ ], [ ])

    for conn in inputready :

        if conn == sock :
            # Terima permintaan koneksi
            conn, client_address = sock.accept()
            # Tambahkan ke list monitor
            list_monitor.append(conn)
        else :
            try :
                # Terima string dari client
                data = conn.recv(100)
                data = data.decode('ascii')
                # Tambah "OK"
                data = "OK "+data
                # Kirim balik ke client
                conn.send(data.encode('ascii'))                
            except(socket.error):
                # Hapus dari list monitor
                list_monitor.remove(conn)
                print("Koneksi ditutup")
                # Tutup koneksi
                conn.close()

    
    