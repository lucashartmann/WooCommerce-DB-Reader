from api import API
from database import Shelve

dados = Shelve.carregar("dados.db", "login")
if dados:
            API.wcapi.url = dados[0]
            API.wcapi.consumer_key = dados[1]
            API.wcapi.consumer_secret = dados[2]
            
data = {
    "name" : "Lucas",
    "email" : "lucas@email.com",
    "username": "lucas123"
}

print(API.adicionar("customers", data))

print(API.get_lista_itens("customers"))