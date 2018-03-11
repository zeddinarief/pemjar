a = input("masukkan angka : ")
for i in range(0,int(a)):
	for x in range(0,i):
		print("* " , end='')
	print("")

print("")

for i in range(int(a),0,-1):
	for x in range(0,i):
		print("* " , end='')
	print("")