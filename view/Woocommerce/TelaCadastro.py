from textual.containers import Container
from textual.widgets import Button, Static, Input, Select
from textual.message import Message
from controller import Controller


class CadastroRealizado(Message):
    def __init__(self) -> None:
        super().__init__()


class TelaCadastro(Container):

    montou = False
    valor_select = ""
    tabela = "products"

    def compose(self):
        # yield Static("ID", id="sttc_id")
        # yield Input(placeholder="id aqui")
        yield Static("Nome")
        yield Input(placeholder="nome aqui", id="stt_nome")
        yield Static("Preço")
        yield Input(placeholder="preço aqui")
        yield Static("Descrição")
        yield Input(placeholder="Descrição aqui", id="input_descricao")
        yield Select([("Products", "Products"), ("Orders", "Orders"), ("Customers", "Customers"), ("Coupons", "Coupons")], allow_blank=False)
        yield Select([("Adicionar", "Adicionar"), ("Editar", "Editar"), ("Remover", "Remover")], allow_blank=False, id="select_operacoes")
        yield Button("Executar")

    def on_select_changed(self, evento: Select.Changed):
        self.query(Static)[1].styles.display = "block"
        self.query(Input)[1].styles.display = "block"
        self.query(Static)[2].styles.display = "block"
        self.query(Input)[2].styles.display = "block"

        match evento.select.value:

            case "Products":
                self.tabela = "products"
                self.query(Static)[1].update("Preço")
                self.query(Input)[1].placeholder = "Preço aqui"
                self.query(Static)[0].update("Nome")
                self.query(Input)[0].placeholder = "Nome aqui"
                self.query(Static)[2].update("Descrição")
                self.query(Input)[2].placeholder = "Descrição aqui"
            case "Customers":
                self.tabela = "customers"
                self.query(Static)[1].update("Email")
                self.query(Input)[1].placeholder = "Email aqui"
                self.query(Static)[0].update("Nome")
                self.query(Input)[0].placeholder = "Nome aqui"
                self.query(Static)[2].styles.display = "none"
                self.query(Input)[2].styles.display = "none"
            case "Coupons":
                self.tabela = "coupons"
                self.query(Static)[0].update("Código")
                self.query(Input)[0].placeholder = "Código aqui"
                self.query(Static)[1].update("Quantidade de desconto:")
                self.query(Input)[
                    1].placeholder = "Quantidade de desconto: aqui"
                self.query(Static)[2].update("Data de expiração")
                self.query(Input)[2].placeholder = "Data de expiração aqui"
            case "Orders":
                self.tabela = "orders"
                self.query(Static)[0].update("Id do cliente")
                self.query(Input)[0].placeholder = "Id do cliente aqui"
                self.query(Static)[1].styles.display = "none"
                self.query(Input)[1].styles.display = "none"
                self.query(Static)[2].styles.display = "none"
                self.query(Input)[2].styles.display = "none"

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
                if self.montou:
                    self.query_one("#stt_id_pesquisa", Static).remove()
                    self.query_one("#inpt_id_pesquisa", Input).remove()
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
                atualizacao = Controller.atualizar_item(
                    self.tabela, id_produto, dados)
                self.notify(atualizacao)
                self.post_message(CadastroRealizado())

            case "Adicionar":
                dados = []
                for input in self.query(Input):
                    dados.append(input.value)
                adicao = Controller.adicionar_item(self.tabela, dados)
                self.notify(adicao)
                self.post_message(CadastroRealizado())

            case "Remover":
                id_produto = self.query_one("#inpt_id_pesquisa", Input).value
                remocao = Controller.remover_item(self.tabela, id_produto)
                self.notify(remocao)
                self.post_message(CadastroRealizado())
