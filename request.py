import requests
url = 'http://127.0.0.1:5000'
r = requests.post(url,json={'exp':1.8,})
print(r.json())