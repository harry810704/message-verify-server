import requests

endpoint = 'http://127.0.0.1:8000/api/product/'

get_res = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello world"})
post_res = requests.post(endpoint, json={"title": "Hello world"})

print(post_res.status_code)
print(post_res.json())
