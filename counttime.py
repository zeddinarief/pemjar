import time
start_time = time.time()
list_angka = [12,3,5,6,7]

print(list_angka[0])

for i in list_angka :
	print (i)
time.sleep(3)
print((time.time() - start_time))