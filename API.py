import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

data = response.json()
print(data)

# posts endpoint

posts = requests.get('https://jsonplaceholder.typicode.com/posts')

data_new = posts.json()
