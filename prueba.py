import requests
import json

URL = "http://www.omdbapi.com/?s={}&apikey=aea5dc7b"

peli = input("Buscar: ")

respuesta = requests.get(URL.format(peli))

mijson = respuesta.json()

print(mijson.get("Search") [0].get("Title"))
print(mijson.get("Search") [0].get("Poster"))
