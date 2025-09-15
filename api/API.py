from woocommerce import API

wcapi = API(
    url="https://sualoja.com",
    consumer_key="ck_xxxxxxxxxxxxxxxxxxxxxx",
    consumer_secret="cs_xxxxxxxxxxxxxxxxxxxxxx",
    version="wc/v3"
)


def adicionar():
    data = {
        "name": "Camiseta",
        "type": "simple",
        "regular_price": "29.90",
        "description": ""
    }

    resposta = wcapi.post("products", data).json()
    return resposta


def remover(id_produto):
    resposta = wcapi.delete(f"products/{id_produto}").json()
    return resposta


def atualizar(id_produto):
    novo_preco = {
        "regular_price": "34.90"
    }

    resposta = wcapi.put(f"products/{id_produto}", novo_preco).json()
    return resposta


def get_lista_produtos():
    lista_de_dicionarios = wcapi.get("products").json()
    return lista_de_dicionarios
