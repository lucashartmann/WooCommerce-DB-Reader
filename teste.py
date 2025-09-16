from api import API
from database import Shelve

dados = Shelve.carregar("dados.db", "login")
if dados:
            API.wcapi.url = dados[0]
            API.wcapi.consumer_key = dados[1]
            API.wcapi.consumer_secret = dados[2]

print(API.atualizar("12", "name", "Camisa Preta"))

print(API.get_lista_produtos())