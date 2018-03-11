#input selalu dianggap sebagai string
angka = input("masukkan sebuah angka ")
#menggunakan int untuk mengconvert menjadi int
c = int(angka) + 30
print(c)
#menggunakan str karena tidak bisa digabung str dan number
print("hasil penjumlahan adalah "+str(c))