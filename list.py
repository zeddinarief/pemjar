import time
list_angka = ["a","b","m","u","p"]

#print(list_angka[0])
print(len(list_angka))
x = 3
for i in list_angka :
	print(i)
list_angka.append("aaaa")
del list_angka[1]
time.sleep(1)
print("-------------------------------")
print(len(list_angka))
a = 0
for i in list_angka :
	print(list_angka[a])
	a+=1

print("-------------------------------")
if len(list_angka) > 0 :
	print("integer")
else :
	print("guduk integer")
