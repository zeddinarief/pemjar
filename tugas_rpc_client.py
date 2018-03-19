import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

print("Menu :")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pengecekan bilangan prima")
menu = input("Masukkan menu : ")

if menu == "1" or menu == "penjumlahan":
	a = input("Angka pertama : ")
	b = input("Angka kedua : ")	
	hasil = proxy.penjumlahan(int(a), int(b))
	print("Hasil penjumlahan = "+str(hasil))

elif menu == "2" or menu == "pengurangan":
	a = input("Angka pertama : ")
	b = input("Angka kedua : ")	
	hasil = proxy.pengurangan(int(a), int(b))
	print("Hasil pengurangan = "+str(hasil))

elif menu == "3" or menu == "perkalian":
	a = input("Angka pertama : ")
	b = input("Angka kedua : ")	
	hasil = proxy.perkalian(int(a), int(b))
	print("Hasil perkalian = "+str(hasil))

elif menu == "4" or menu == "pembagian":
	a = input("Angka pertama : ")
	b = input("Angka kedua : ")	
	hasil = proxy.pembagian(int(a), int(b))
	print("Hasil pembagian = "+str(hasil))

elif menu == "5" or menu == "prima":
	a = int(input("Masukkan angka : "))	
	hasil = proxy.prima(int(a))
	print(hasil)
