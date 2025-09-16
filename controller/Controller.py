from api import API


def adicionar_produto(dados):
    preco = dados[0]
    nome = dados[1]

    # data = {
    #         "name": "Camiseta",
    #         "type": "simple",
    #         "regular_price": "29.90",
    #         "description": ""
    #     }

    data = {
            "name": f"{nome}",
            "regular_price": f"{preco}",
        }

    adicao = API.adicionar(data)

    if adicao:
        return "Produto adicionado com sucesso!"
    return f"ERRO! Não foi possivel adicionar produto"


def remover_produto(id_produto):
    if id_produto == "":
        return "ID está vazio"

    remocao = API.remover(id_produto)

    if remocao:
        return "Produto removido com sucesso"
    return f"ERRO! Não foi possivel remover produto '{id_produto}'"


def atualizar_produto(id_produto, dados):
    if id_produto == "":
        return "ID está vazio"

    novo_preco = dados[0]
    novo_nome = dados[1]

    resultado_atualizacao = ""

    if novo_preco:
        atualizacao = API.atualizar(id_produto, "price", novo_preco)
        if atualizacao:
            resultado_atualizacao += "Preço atualizado com sucesso com sucesso"
        else:
            resultado_atualizacao += f"ERRO! Não foi possivel atualizar preço do produto '{id_produto}'"

    if novo_nome:
        atualizacao = API.atualizar(id_produto, "name", novo_nome)
        if atualizacao:
            resultado_atualizacao += "Nome atualizado com sucesso com sucesso"
        else:
            resultado_atualizacao += f"ERRO! Não foi possivel atualizar o nome do produto '{id_produto}'"

    return resultado_atualizacao


def consultar_produto_por_id(id_produto):
    if id_produto == "":
        return "ID está vazio"

    consulta = API.get_produto(id_produto)

    if consulta:
        return consulta
    return f"ERRO! Não foi possivel consultar produto '{id_produto}'"
