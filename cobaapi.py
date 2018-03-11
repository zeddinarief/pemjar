import urllib.request, json 

isbn = input("isbn number : ")
with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn) as url:
    data = json.loads(url.read().decode())
    print(data)