def send_termination(conn,data):
	term_char = "\r\n"
	data = data+term_char
	conn.send(data.encode('ascii'))

def recv_termination(conn):
	#variabel untuk mnampung data
	data = ''
	while True:
		#baca pkai recv
		buffer = conn.recv(20)
		buffer = buffer.decode('ascii')
		#cek jika buffer mengandung termination char
		if "\r\n" in buffer:
			#buang termination char
			data = data.replace("\r\n", "")
			#tambah buffer ke data
			data = data+buffer
			#keluar dari fungsi
			return data
		#tambah buffer ke data
		data = data+buffer

def send_size(conn,data):
	#hitung ukuran data
	size = len(data)
	#pack variabel size
	size = struct.pack("<I",size)
	#encode data
	data = data.encode('ascii')
	data = size+data
	conn.send(data)

def recv_size(conn):
	def recv_size(conn):
    #baca ukuran data int = 4byte
    size = conn.recv(4)
    size = struct.unpack("<I", size)[0]
    #baca data
    data = conn.recv(size)
    #decode
    data = data.decode('ascii')
    return data