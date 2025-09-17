from api import API
from database import Shelve

dados = Shelve.carregar("dados.db", "login")
if dados:
            API.wcapi.url = dados[0]
            API.wcapi.consumer_key = dados[1]
            API.wcapi.consumer_secret = dados[2]
            
data = {
    "status": "processing",
    "customer_id": "271481149",
    "currency" : "BRL" 
}

print(API.adicionar("orders", data))

print(API.get_lista_itens("orders"))