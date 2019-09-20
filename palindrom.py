angka = 923325595
# mengubah integer menjadi string terlebih dahulu
strangka = str(angka)

def palindrom(x):
	# membuat array untuk menyimpan string angka yang nantinya akan menyimpan hasil akhir palindrom
	arr = []
	for x in strangka:
	    arr.append(x)
	    
	# menyimpan angka-angka yang berpasangan ke dalam array
	arr_couple = []
	# menyimpan angka yang tidak berpasangan(kurang dari 2 atau lebih dari 2  dalam array
	arr_notcouple = []

	# menyimpan angka yang sudah di cari kedalam array agar tidak terjadi pencarian ulang
	arr_done = []

	# mencari angka yang berpasangan terlebih dahulu
	for x in strangka:
	    # variabel a nantinya untuk menghitung berapa banyak angka yang ditemukan
	    a = 0
	    # dilihat apakah angka sudah ada pernah dicari berdasarkan isi arr_done
	    if x in arr_done:
	        pass
	    else:
	        # mencari berapa kali angka ditemukan
	        for y in range(len(strangka)):
	            if x == strangka[y]:
	                a += 1
	        # jika ditemukan berpasangan
	        if a == 2:
	            arr_couple.append(x)
	        # jika tidak berpasangan
	        else:
	            # disini array not couple index 0 digunakan menyimpan angka non couple dan index 1 untuk menyimpan banyak angka noncouple
	            arr_notcouple.append(x)
	            arr_notcouple.append(a)
	    # menyimpan angka yg sudah dicari ke array arr_done
	    arr_done.append(x)

	# merupakan variabel untuk menunjukkan index array arr[]
	a = 1 
	# mengganti isi array arr[] dengan angka yang berpasangan dahulu
	lenstr = len(arr)
	for x in arr_couple:
	    # angka dimulai index paling awal dan paling akhir
	    arr[a-1] = x
	    arr[lenstr-a] = x
	    a += 1
	    
	# ketika tidak ditemukan angka non coupel/ semuanya couple
	if len(arr_notcouple) == 0:
	    for x in arr:
	        print(x, end="")
	else:
	    # panjang array couple digunakan untuk menentukan index awal untuk meletakkan angka non couple
	    lenstrcouple = len(arr_couple)
	    for x in range(int(arr_notcouple[1])):
	        arr[lenstrcouple] = arr_notcouple[0]
	        lenstrcouple += 1
	    
	    # untuk mencetak output
	    result = ""
	    for x in arr:
	        result += x
	        # print(x, end="")
	    return result

arr_angka = []
for x in strangka:
	arr_angka.append(x)

arr_result = []
for x in range(len(arr_angka)):
	arr_angka.append(arr_angka[0])
	arr_angka.pop(0)
	strangka = ""
	for x in arr_angka:
		strangka += x

	output = palindrom(strangka)
	if output in arr_result:
		pass
	else:
		arr_result.append(output)

print(arr_result)
