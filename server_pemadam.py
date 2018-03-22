# Import socket
import socket
import select
import json
# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke address dan port tertentu
sock.bind( ('0.0.0.0', 6667) )

# Listen sebanyak 100 permintaan koneksi
sock.listen(100)

list_monitor = [ sock ]
#laporan = []

while True :

    inputready, outputready, errorreadey = select.select(list_monitor, [ ], [ ])

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
                datasp = data.split(',')

                if datasp[0] == "petugas":
                    files = open("data.txt","r")
                    respon = files.read()
                    files.close()
                else:  
                    files = open("data.txt","w")
                    files.write("nama : "+ datasp[0] + "\nalamat : "+datasp[1])
                    respon = "OK"
                    files.close()
                '''
                nama = data.json['nama']
                alamat = data.json['alamat']
                
                laporan_baru = {
                    'nama' : nama,
                    'alamat' : alamat
                }
                
                laporan.append(laporan_baru)    
                '''
                # Kirim balik ke client
                conn.send(respon.encode('ascii'))

            except(socket.error):
                # Hapus dari list monitor
                list_monitor.remove(conn)
                print("Koneksi ditutup")
                # Tutup koneksi
                conn.close()
'''
    for conn in outputready:
        if conn != list_monitor[0] && conn != list_monitor[1]

        else :
            try:
                open    
             except (socket.error):
                 raise
'''          
    