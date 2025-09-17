from api import API


def adicionar_item(tabela, dados):

    match tabela:

        case "orders":
            id_cliente = dados[0]

            data = {
                "customer_id": id_cliente
            }

        case "coupons":
            codigo = dados[0]
            quantidade_desconto = dados[1]
            data_expiracao = dados[2]

            data = {
                "code": codigo,
                "amount": quantidade_desconto,
                "date_expires": data_expiracao
            }

        case "products":
            preco = dados[1]
            nome = dados[0]
            descricao = dados[2]

            data = {
                "name": nome,
                "regular_price": preco,
                "description": descricao
            }

        case "customers":
            email = dados[1]
            nome = dados[0]

            nome_split = nome.split()

            if len(nome_split) > 1:
                data = {
                    "email": email,
                    "first_name": nome_split[:-1],
                    "last_name": nome_split[-1]
                }
            else:
                data = {
                    "email": email,
                    "first_name": nome,
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

    resultado_atualizacao = ""

    match tabela:

        case "orders":
            id_cliente = dados[0]

            if id_cliente:
                atualizacao = API.atualizar(
                    tabela, id_item, "customer_id", id_cliente)
                if atualizacao:
                    resultado_atualizacao += "ID do cliente atualizado com sucesso com sucesso"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar o ID do cliente de '{id_item}'"

        case "coupons":
            codigo = dados[0]
            quantidade_desconto = dados[1]
            data_expiracao = dados[2]

            if codigo:
                atualizacao = API.atualizar(tabela, id_item, "code", codigo)
                if atualizacao:
                    resultado_atualizacao += "Código atualizado com sucesso com sucesso\n"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar o código de '{id_item}'\n"

            if quantidade_desconto:
                atualizacao = API.atualizar(
                    tabela, id_item, "amount", quantidade_desconto)
                if atualizacao:
                    resultado_atualizacao += "Quantidade de desconto atualizado com sucesso com sucesso\n"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar a quantidade de desconto de '{id_item}'\n"

            if data_expiracao:
                atualizacao = API.atualizar(
                    tabela, id_item, "date_expires", data_expiracao)
                if atualizacao:
                    resultado_atualizacao += "data_expiracao atualizado com sucesso com sucesso"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar o data_expiracao de '{id_item}'"

        case "products":
            preco = dados[1]
            nome = dados[0]
            descricao = dados[2]

            if preco:
                atualizacao = API.atualizar(tabela, id_item, "regular_price", preco)
                if atualizacao:
                    resultado_atualizacao += "Preço atualizado com sucesso com sucesso\n"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar preço de '{id_item}' \n"

            if nome:
                atualizacao = API.atualizar(tabela, id_item, "name", nome)
                if atualizacao:
                    resultado_atualizacao += "Nome atualizado com sucesso com sucesso\n"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar o nome de '{id_item}'\n"

            if descricao:
                atualizacao = API.atualizar(
                    tabela, id_item, "description", descricao)
                if atualizacao:
                    resultado_atualizacao += "Descrição atualizado com sucesso com sucesso"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar a descrição de '{id_item}'"

        case "customers":
            email = dados[0]
            nome = dados[1]

            if email:
                atualizacao = API.atualizar(tabela, id_item, "email", email)
                if atualizacao:
                    resultado_atualizacao += "Preço atualizado com sucesso com sucesso"
                else:
                    resultado_atualizacao += f"ERRO! Não foi possivel atualizar preço de '{id_item}'"

            nome_split = nome.split()

            if nome:
                if len(nome_split) > 1:
                    atualizacao = API.atualizar(
                        tabela, id_item, "first_name", nome_split[:-1])
                    if atualizacao:
                        resultado_atualizacao += "Nome atualizado com sucesso com sucesso\n"
                    else:
                        resultado_atualizacao += f"ERRO! Não foi possivel atualizar o nome de '{id_item}'\n"

                    atualizacao = API.atualizar(
                        tabela, id_item, "last_name", nome_split[-1])
                    if atualizacao:
                        resultado_atualizacao += "Nome atualizado com sucesso com sucesso\n"
                    else:
                        resultado_atualizacao += f"ERRO! Não foi possivel atualizar o nome de '{id_item}'\n"
                else:

                    atualizacao = API.atualizar(
                        tabela, id_item, "first_name", nome)
                    if atualizacao:
                        resultado_atualizacao += "Nome atualizado com sucesso com sucesso\n"
                    else:
                        resultado_atualizacao += f"ERRO! Não foi possivel atualizar o nome de '{id_item}'\n"

                    atualizacao = API.atualizar(
                        tabela, id_item, "last_name", "")
                    if atualizacao:
                        resultado_atualizacao += "Nome atualizado com sucesso com sucesso"
                    else:
                        resultado_atualizacao += f"ERRO! Não foi possivel atualizar o nome de '{id_item}'"

    return resultado_atualizacao


def consultar_item_por_id(tabela, id_item):
    if id_item == "":
        return "ID está vazio"

    consulta = API.get_item(tabela, id_item)

    if consulta:
        return consulta
    return f"ERRO! Não foi possivel consultar '{id_item}'"
