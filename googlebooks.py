import urllib.request, json 

isbn = input("isbn number : ")
api_key = "AIzaSyAqd-hGvKYCUu4ueaLKo9dVFt65pJ2zOYg"
with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn+"&key="+api_key) as url:
    data = json.loads(url.read())
    print("judul : "+data["items"][0]["volumeInfo"]["title"])
    print("pengarang : ")
    for i in data["items"][0]["volumeInfo"]["authors"]:
    	print("-"+i)
    print("penerbit : "+data["items"][0]["volumeInfo"]["publisher"])
    print("tahun penerbit : "+data["items"][0]["volumeInfo"]["publishedDate"])
