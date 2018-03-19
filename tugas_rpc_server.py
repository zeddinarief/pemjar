import xmlrpc.server

server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )

def penjumlahan(a,b):
	return(a+b)

def pengurangan(a,b):
	return(a-b)

def perkalian(a,b):
	return(a*b)

def pembagian(a,b):
	return(a/b)

def prima(a):
	if a == 2:
		hasil = "adalah bilangan prima"
	elif a > 2:
		for i in range(2,a):
			if (a % i) == 0:
				hasil = "bukan bilangan prima"
				break
			else:
				hasil = "adalah bilangan prima"
	else:
		hasil = "bukan bilangan prima!"
	return(hasil)

server.register_function(prima, 'prima')
server.register_function(pembagian, 'pembagian')
server.register_function(perkalian, 'perkalian')
server.register_function(pengurangan, 'pengurangan')
server.register_function(penjumlahan, 'penjumlahan')
server.serve_forever()


