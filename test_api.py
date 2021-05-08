import requests

x = requests.get('https://deploy-model-cactus.herokuapp.com/predict?humidity=61.33&temp=26.64&soil=35.47')
x = x.json()
print(x["result"])