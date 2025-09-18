from api import API


def adicionar_item(tabela, dados: dict):
    if tabela == "customers" and "name" in dados.keys():

        nome_split = dados["name"].split()

        if len(nome_split) > 1:
            dados["first_name"] = nome_split[:-1]
            dados["last_name"] = nome_split[-1]
            del dados["name"]

    adicao = API.adicionar(tabela, dados)

    if adicao:
        return "Cadastro realizado com sucesso!"
    return f"ERRO! Não foi possivel realizar cadastro"


def remover_item(tabela, id_item):
    if id_item == "":
        return "ID está vazio"
    
    consulta = API.get_item(tabela, id_item)
    if not consulta:
        return f"Não existe item com id '{id_item}'"

    remocao = API.remover(tabela, id_item)

    if remocao:
        return "Remoção realizada com sucesso"
    return f"ERRO! Não foi possivel remover '{id_item}'"


def atualizar_item(tabela, id_item, dados):
    if id_item == "":
        return "ID está vazio"
    
    consulta = API.get_item(tabela, id_item)
    if not consulta:
        return f"Não existe item com id '{id_item}'"

    resultado_atualizacao = ""

    if tabela == "customers" and "name" in dados.keys() and dados["name"]:

        nome_split = dados["name"].split()

        if len(nome_split) > 1:
            dados["first_name"] = nome_split[:-1]
            dados["last_name"] = nome_split[-1]
            del dados["name"]

    for chave, valor in dados.items():
        if valor: 
            
            atualizacao = API.atualizar(tabela, id_item, chave, valor)
            if atualizacao:
                resultado_atualizacao += f"{chave.capitalize()} atualizado com sucesso com sucesso\n"
            else:
                resultado_atualizacao += f"ERRO! Não foi possivel atualizar {chave} de '{id_item}'"

    return resultado_atualizacao