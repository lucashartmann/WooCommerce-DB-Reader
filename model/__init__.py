from api import API
from database import Shelve
from model import Produto, Pedido, Cliente, Cupom, Taxa


class Init:

    um_produto = Produto.Produto()
    um_cliente = Cliente.Cliente("asds")
    um_pedido = Pedido.Pedido()
    um_cupom = Cupom.Cupom("qwdsadas")
    uma_taxa = Taxa.Taxa()

    dict_objetos = {
        "products": um_produto, "orders": um_pedido,  "customers": um_cliente, "coupons": um_cupom,   "taxes": uma_taxa
    }

    dados = Shelve.carregar("dados.db", "login")
    if dados:
        API.wcapi.url = dados[0]
        API.wcapi.consumer_key = dados[1]
        API.wcapi.consumer_secret = dados[2]

    if len(API.get_lista_itens("customers")) < 1:

        data = {
            "email": "lucas@email.com",
            "first_name": "Lucas",
            "last_name": "Bastos",
            "username": "ddelux19"
        }

        print(API.adicionar("customers", data))

        print(API.get_lista_itens("customers"))

    if len(API.get_lista_itens("coupons")) < 1:

        data = {
            "email": "free shipping",
            "first_name": "0.00",
            "last_name": "fixed_cart",
        }

        print(API.adicionar("coupons", data))

        print(API.get_lista_itens("coupons"))

    if len(API.get_lista_itens("products")) < 1:

        data = {
        }

        print(API.adicionar("products", data))

        print(API.get_lista_itens("products"))

    if len(API.get_lista_itens("orders")) < 1:

        data = {
            "status": "processing",
            "customer_id": "271481149",
            "currency": "BRL"
        }

        print(API.adicionar("orders", data))

        print(API.get_lista_itens("orders"))
