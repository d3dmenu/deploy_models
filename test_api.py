import requests

x = requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(x.text, type(x))