from woocommerce import API

wcapi = API(
    url="https://sualoja.com",
    consumer_key="ck_xxxxxxxxxxxxxxxxxxxxxx",
    consumer_secret="cs_xxxxxxxxxxxxxxxxxxxxxx",
    version="wc/v3"
)


def adicionar(dados:dict):
    try:
        # data = {
        #     "name": "Camiseta",
        #     "type": "simple",
        #     "regular_price": "29.90",
        #     "description": ""
        # }

        wcapi.post("products", dados).json()
        return True
    except Exception as e:
        print("ERRO!", e)
        return None


def remover(id_produto):
    try:
        wcapi.delete(f"products/{id_produto}").json()
        return True
    except Exception as e:
        print("ERRO!", e)
        return None


def atualizar(id_produto, tipo_dado, novo_valor):
    try:
        # novo_preco = {
        #     "regular_price": "34.90"
        # }

        novo_dado = {
            tipo_dado: novo_valor
        }

        wcapi.put(f"products/{id_produto}", novo_dado).json()
        return True
    except Exception as e:
        print("ERRO!", e)
        return None


def get_lista_produtos():
    try:
        lista_de_dicionarios = wcapi.get("products").json()
        if not lista_de_dicionarios:
            return []
        return lista_de_dicionarios
    except Exception as e:
        print("ERRO!", e)
        return []


def get_produto(id_produto):
    try:
        lista_de_dicionarios = wcapi.get(f"products/{id_produto}").json()
        if not lista_de_dicionarios:
            return []
        return lista_de_dicionarios
    except Exception as e:
        print("ERRO!", e)
        return []
