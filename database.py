import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root',password='',host='localhost',database='nmstelkom')

# prepare a cursor object using cursor() method
cursor = db.cursor()
#p = "192.168.100.99"
# execute SQL query using execute() method.
#cursor.execute("SELECT sid, ip FROM customer WHERE ip='%s'" %(p))
cursor.execute("SELECT ip FROM customer")
# Fetch a single row using fetchone() method.
data = cursor.fetchall()
num = cursor.rowcount
print (num)
print(data)
print("---------------------")
for row in data:
	print (row[0])
	#print(cursor.rowcount)
print("---------------------")
a = "192.168.21.1"
if a in data :
	print("ada")
else :
	print("tidak ada")
print("---------------------")

arr = ["192.168.1.1","192.168.1.3"]
if a in arr :
	print("ada")
else :
	print("tidak ada")
	
db.close()
