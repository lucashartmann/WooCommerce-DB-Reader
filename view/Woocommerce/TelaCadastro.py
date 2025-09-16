from textual.containers import Container, HorizontalGroup
from textual.widgets import Button, Static, Input, Select
from textual import on
from textual.message import Message
from controller import Controller


class CadastroRealizado(Message):
    def __init__(self) -> None:
        super().__init__()


class TelaCadastro(Container):

    montou = False
    valor_select = ""

    def compose(self):
        # yield Static("ID", id="sttc_id")
        # yield Input(placeholder="id aqui")
        yield Static("Preço")
        yield Input(placeholder="preço aqui")
        yield Static("Nome")
        yield Input(placeholder="nome aqui", id="stt_nome")

        yield Select([("Adicionar", "Adicionar"), ("Editar", "Editar"), ("Remover", "Remover")], allow_blank=False)
        yield Button("Executar")

    def on_select_changed(self, evento: Select.Changed):
        if self.montou:
            self.query_one("#stt_id_pesquisa", Static).remove()
            self.query_one("#inpt_id_pesquisa", Input).remove()

        match evento.select.value:
            case "Editar":
                if self.montou == False:
                    self.mount(Static("ID de pesquisa",
                                      id="stt_id_pesquisa"), before=0)
                    self.mount(Input(placeholder="id do produto de pesquisa",
                                     id="inpt_id_pesquisa"), before=1)
                    self.montou = True
                self.valor_select = "Editar"

            case "Adicionar":
                self.valor_select = "Adicionar"
                self.montou = False

            case "Remover":
                if self.montou == False:
                    self.mount(Static("ID de pesquisa",
                                      id="stt_id_pesquisa"), before=0)
                    self.mount(Input(placeholder="id do produto de pesquisa",
                                     id="inpt_id_pesquisa"), before=1)
                    self.montou = True
                self.valor_select = "Remover"

    def on_button_pressed(self):
        match self.valor_select:
            case "Editar":
                id_produto = self.query_one("#inpt_id_pesquisa", Input).value
                dados = []
                for input in self.query(Input)[1:]:
                    dados.append(input.value)
                atualizacao = Controller.atualizar_produto(id_produto, dados)
                self.notify(atualizacao)
                self.post_message(CadastroRealizado())

            case "Adicionar":
                dados = []
                for input in self.query(Input):
                    dados.append(input.value)
                adicao = Controller.adicionar_produto(dados)
                self.notify(adicao)
                self.post_message(CadastroRealizado())

            case "Remover":
                id_produto = self.query_one("#inpt_id_pesquisa", Input).value
                remocao = Controller.remover_produto(id_produto)
                self.notify(remocao)
                self.post_message(CadastroRealizado())
