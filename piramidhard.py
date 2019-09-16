
masukan = int(input('masukkan tinggi piramid : '))
arr1 = []
arr2 = []
arr3 = []
a = 1
b = 2
c = 3

for x in range(masukan):
	arr1.append(a)
	arr2.append(b)
	arr3.append(c)
	a += 3
	b += 3
	c += 3

print(arr1)
print(arr2)
print(arr3)
print(masukan)
for x in range(1, masukan + 1):
	for y in range(1, x+1):
		if y in arr1:
			print('#', end="")
		elif y in arr2:
			print('$', end="")
		elif y in arr3:
			print('%', end="")
	print()
