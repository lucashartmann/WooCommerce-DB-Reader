from view import App
import sys
from controller import Controller

comando = sys.argv[1:]


def menu(comando):
    match comando:
        case ["login", url, consumer_key, cosumer_secret]:
            dados = [url, consumer_key, cosumer_secret]
            Controller.salvar_login(dados)
        case ["cadastrar", tabela]:
            dados = comando[2:]
            print(Controller.adicionar_item(tabela.lower(), dados))
        case ["remover", tabela, id]:
            print(Controller.remover_item(tabela.lower(), id))
        case ["atualizar", tabela, id]:
            dados = comando[3:]
            print(Controller.atualizar_item(tabela.lower(), id, dados))
        case ["listar", tabela]:
            print(Controller.listar_itens(tabela.lower()))
        case ["consultar", tabela, id]:
            print(Controller.consultar_item(tabela.lower(), id))
        case _:
            print("ERRO! Comando inválido!")


if __name__ == "__main__":
    if len(comando) > 0:
        menu(comando)
    else:
        app = App.App()
        app.run()
