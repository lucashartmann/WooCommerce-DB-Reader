from api import API


def adicionar_item(tabela, dados):
    
    if tabela == "products":
        preco = dados[0]
        nome = dados[1]
        
        data = {
            "name": f"{nome}",
            "regular_price": f"{preco}",
        }
        
    elif tabela == "customers":
        email = dados[0]
        nome = dados[1]

        data = {
            "email": f"{email}",
            "name": f"{nome}",
        }

    adicao = API.adicionar(tabela, data)

    if adicao:
        return "Cadastro realizado com sucesso!"
    return f"ERRO! Não foi possivel realizar cadastro"


def remover_item(tabela, id_item):
    if id_item == "":
        return "ID está vazio"

    remocao = API.remover(tabela, id_item)

    if remocao:
        return "Remoção realizada com sucesso"
    return f"ERRO! Não foi possivel remover '{id_item}'"


def atualizar_item(tabela, id_item, dados):
    if id_item == "":
        return "ID está vazio"

    novo_preco = dados[0]
    novo_nome = dados[1]

    resultado_atualizacao = ""

    if novo_preco:
        atualizacao = API.atualizar(tabela, id_item, "price", novo_preco)
        if atualizacao:
            resultado_atualizacao += "Preço atualizado com sucesso com sucesso"
        else:
            resultado_atualizacao += f"ERRO! Não foi possivel atualizar preço de '{id_item}'"

    if novo_nome:
        atualizacao = API.atualizar(tabela, id_item, "name", novo_nome)
        if atualizacao:
            resultado_atualizacao += "Nome atualizado com sucesso com sucesso"
        else:
            resultado_atualizacao += f"ERRO! Não foi possivel atualizar o nome de '{id_item}'"

    return resultado_atualizacao


def consultar_item_por_id(tabela, id_item):
    if id_item == "":
        return "ID está vazio"

    consulta = API.get_produto(tabela, id_item)

    if consulta:
        return consulta
    return f"ERRO! Não foi possivel consultar '{id_item}'"
