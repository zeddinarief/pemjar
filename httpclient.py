import http.client

#buka koneksi
conn = http.client.HTTPConnection("filkom.ub.ac.id")
#kirim request
req = conn.request("GET", "/")
#baca respon
respon = conn.getresponse()
#print header
print("headernya adalah : ")
print(respon.getresponse())
#print payload
print("payloadnya adalah : ")
print(respon.read())