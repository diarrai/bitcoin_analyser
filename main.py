import requests
import json
from api_config import API_KEY

BASE_URL = 'https://rest.coinapi.io/'
url = BASE_URL + 'v1/assets'
headers = {'X-CoinAPI-Key': API_KEY}
response = requests.get(url, headers=headers)
# Gestion d'erreur si la cle API est incorrecte
#Deserialisons le format json
if response.status_code == 200:
   print("L'appel a l'API a fonctionne")
   data = json.loads(response.text)
#Recuperons les 10 premieres donnees
   nb_assets = len(data)
   #asset_id
   #name
   print("Nombre d'assets monetaires:", nb_assets)
   if nb_assets >= 10:
       for i in range(10):
           d = data[i]
           print(d["asset_id"] + ": " + d["name"])
   print()
   print("Quota Restant", response.headers["x-ratelimit-remaining"])
else:
    #cas d'erreur 22676047608
    print("L'appel a l'API a retourner une erreur: ", response.status_code)

#Obervons ce qu'on a au debogueur
