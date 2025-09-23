from view import App
import sys
from controller import Controller
from database import Shelve


comando = sys.argv[1:]


def login():
    dados = Shelve.carregar("dados.db", "login")
    if dados:
        Controller.carregar_login(dados)
    else:
        print("Faça Login antes! [login url consumer_key cosumer_secret]")
        return


def help():
    comandos = '''
TABELAS: products, customers, orders, coupons

        ######### COMANDOS ###########

AJUDA: "ajuda" ou "--help" ou "help" ou "--ajuda"

lOGIN: "login" url consumer_key cosumer_secret
Exemplo: login https://sualoja.com ck_xxxxxxxxxxxxxxxxxxxxxx cs_xxxxxxxxxxxxxxxxxxxxxx

CADASTRO: "cadastrar" nome_da_tabela
*produtos: cadastrar products "name" "price" "description"
*clientes: cadastrar customers "email" "first_name" "last_name"
*pedidos: cadastrar orders "customer_id"
*cupons: cadastrar coupons "code" "amount" "date_expires"

Exemplo: cadastrar products "Camisa Social" "200.80" "Camisa vermelha slim para festas"
Exemplo: cadastrar customers "john@email.com" "John Doe" 
Exemplo: cadastrar orders 54
Exemplo: cadastrar coupons 345634 10 "date_expires"

REMOÇÃO: "remover" nome_da_tabela id_do_item
Exemplo: remover products 60

ATUALIZAÇÃO: "atualizar" nome_da_tabela id_do_item
*produtos: atualizar products "name" "price" "description"
*clientes: atualizar customers "email" "first_name" "last_name"
*pedidos: atualizar orders "customer_id"
*cupons: atualizar coupons "code" "amount" "date_expires"

Exemplo: atualizar products "Toalha de Mesa" "30.848" "Toalha florida impermeável"
Exemplo: atualizar customers "lucas@email.com" "Lucas Doe" 
Exemplo: atualizar orders 30
Exemplo: atualizar coupons 1132 20 "date_expires"

LISTAGEM: "listar" nome_da_tabela
Exemplo: listar customers

CONSULTA: "consultar" nome_da_tabela id_do_item
Exemplo: consultar customers 10
'''
    return comandos


def menu(comando):
    match comando:
        case ["login", url, consumer_key, cosumer_secret]:
            dados = [url, consumer_key, cosumer_secret]
            Controller.salvar_login(dados)
        case ["cadastrar", tabela]:
            dados = comando[2:]
            login()
            print(Controller.adicionar_item(tabela.lower(), dados))
        case ["remover", tabela, id]:
            login()
            print(Controller.remover_item(tabela.lower(), id))
        case ["atualizar", tabela, id]:
            dados = comando[3:]
            login()
            print(Controller.atualizar_item(tabela.lower(), id, dados))
        case ["listar", tabela]:
            login()
            print(Controller.listar_itens(tabela.lower()))
        case ["consultar", tabela, id]:
            login()
            print(Controller.consultar_item(tabela.lower(), id))
        case ["ajuda" | "--help" | "help" | "--ajuda"]:
            print(help())
        case _:
            print("ERRO! Comando inválido!")


if __name__ == "__main__":
    if len(comando) > 0:
        menu(comando)
    else:
        app = App.App()
        app.run()
