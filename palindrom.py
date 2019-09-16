angka =  33228844  # 923325595
strangka = str(angka)
# ini mulai

arr_ex = []
arr_done = []
arr_double = []
arr_notdouble = []
for x in strangka:
	arr_ex.append(x)

# print(arr_ex)

for x in strangka: #huruf nya
	a = 0
	if x in arr_done:
		pass
	else :
		for y in range(len(strangka)): #index nya
			if x == strangka[y]:
				a += 1
		if a == 2:
			arr_double.append(x)
		else :
			arr_notdouble.append(x)
			arr_notdouble.append(a)

		arr_done.append(x)

a = 1
lenstr = len(arr_ex)
for x in arr_double: #huruf
	# print(a)
	arr_ex[a-1] = x
	arr_ex[lenstr-a] = x
	a += 1

if len(arr_notdouble) == 0:
	for x in arr_ex:
		print(x, end="")
else:
	lenstrdouble = len(arr_double)
	for x in range(int(arr_notdouble[1])):
		arr_ex[lenstrdouble] = arr_notdouble[0]
		lenstrdouble += 1
		
	for x in arr_ex:
		print(x, end="")



# print(arr_ex)
# print(arr_double)
# print(arr_notdouble)
# ini akhir
