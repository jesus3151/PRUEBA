import requests 

URL = "https://www.yelp.com/biz/mancinis-wood-fired-pizza-brooklyn-2"

respuesta = requests.get(URL)

print(respuesta)

