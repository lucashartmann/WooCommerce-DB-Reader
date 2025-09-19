from textual.widgets import Button, Static, Input, Select, Tab, Tabs, Header, Footer
from textual.message import Message
from controller import Controller
from unidecode import unidecode
from textual.screen import Screen
from textual.containers import Grid


class TelaCadastro(Screen):

    CSS_PATH = "css/TelaCadastro.tcss"

    montou = False
    valor_select = ""
    tabela = "products"

    def compose(self):
        # yield Static("ID", id="sttc_id")
        # yield Input(placeholder="id aqui")
        yield Header()
        yield Tabs(Tab("TelaCadastrar", id="tab_cadastrar"), Tab("TelaConsultar", id="tab_consultar"))
        with Grid():
            yield Static("Name")
            yield Input(placeholder="nome aqui", id="stt_nome")
            yield Static("Regular_Price")
            yield Input(placeholder="preço aqui")
            yield Static("Description")
            yield Input(placeholder="Descrição aqui", id="input_descricao")
            yield Select([("Products", "Products"), ("Orders", "Orders"), ("Customers", "Customers"), ("Coupons", "Coupons")], allow_blank=False)
            yield Select([("Adicionar", "Adicionar"), ("Editar", "Editar"), ("Remover", "Remover")], allow_blank=False, id="select_operacoes")
            yield Button("Executar")
        yield Footer()

    def on_tabs_tab_activated(self, event: Tabs.TabActivated):
        if event.tabs.active == self.query_one("#tab_consultar", Tab).id:
            self.app.switch_screen("tela_consultar")

    def on_screen_resume(self):
        self.query_one(Tabs).active = self.query_one("#tab_cadastrar", Tab).id

    def on_select_changed(self, evento: Select.Changed):

        if evento.select.id != "select_operacoes":

            self.query_one(Grid).query(Static)[1].styles.display = "block"
            self.query_one(Grid).query(Input)[1].styles.display = "block"
            self.query_one(Grid).query(Static)[2].styles.display = "block"
            self.query_one(Grid).query(Input)[2].styles.display = "block"


            match evento.select.value:

                case "Products":
                    self.tabela = "products"
                    self.query_one(Grid).query(Static)[0].update("Name")
                    self.query_one(Grid).query(Input)[0].placeholder = "Nome aqui"
                    self.query_one(Grid).query(Static)[1].update("Regular_Price")
                    self.query_one(Grid).query(Input)[1].placeholder = "Preço aqui"
                    self.query_one(Grid).query(Static)[2].update("Description")
                    self.query_one(Grid).query(Input)[
                        2].placeholder = "Descrição aqui"
                case "Customers":
                    self.tabela = "customers"
                    self.query_one(Grid).query(Static)[0].update("Name")
                    self.query_one(Grid).query(Input)[0].placeholder = "Name aqui"
                    self.query_one(Grid).query(Static)[1].update("Email")
                    self.query_one(Grid).query(Input)[1].placeholder = "Email aqui"
                    self.query_one(Grid).query(Static)[2].styles.display = "none"
                    self.query_one(Grid).query(Input)[2].styles.display = "none"
                case "Coupons":
                    self.tabela = "coupons"
                    self.query_one(Grid).query(Static)[0].update("Code")
                    self.query_one(Grid).query(Input)[
                        0].placeholder = "Código aqui"
                    self.query_one(Grid).query(Static)[1].update("Amount")
                    self.query_one(Grid).query(Input)[
                        1].placeholder = "Quantidade de desconto: aqui"
                    self.query_one(Grid).query(Static)[
                        2].update("Data de expiração")
                    self.query_one(Grid).query(Input)[
                        2].placeholder = "Data de expiração aqui"
                case "Orders":
                    self.tabela = "orders"
                    self.query_one(Grid).query(Static)[0].update("Customer_ID")
                    self.query_one(Grid).query(Input)[
                        0].placeholder = "Id do cliente aqui"
                    self.query_one(Grid).query(Static)[1].styles.display = "none"
                    self.query_one(Grid).query(Input)[1].styles.display = "none"
                    self.query_one(Grid).query(Static)[2].styles.display = "none"
                    self.query_one(Grid).query(Input)[2].styles.display = "none"

        else:
            match evento.select.value:

                case "Editar":
                    if self.montou == False:
                        self.query_one(Grid).mount(Static("ID de pesquisa",
                                                        id="stt_id_pesquisa"), before=0)
                        self.query_one(Grid).mount(Input(placeholder="id do produto de pesquisa",
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
                    if self.montou:
                        self.query_one("#stt_id_pesquisa", Static).remove()
                        self.query_one("#inpt_id_pesquisa", Input).remove()
                        self.montou = False
                    self.query_one(Grid).query(Static)[0].update("ID")
                    self.query_one(Grid).query(Input)[0].placeholder = "Id aqui"
                    self.query_one(Grid).query(Static)[1].styles.display = "none"
                    self.query_one(Grid).query(Input)[1].styles.display = "none"
                    self.query_one(Grid).query(Static)[2].styles.display = "none"
                    self.query_one(Grid).query(Input)[2].styles.display = "none"
                    self.valor_select = "Remover"

    def limpar_inputs(self):
        for input in self.query(Input):
            input.value = ""

    def on_button_pressed(self):
        match self.valor_select:
            case "Editar":
                id_produto = self.query_one("#inpt_id_pesquisa", Input).value
                dados = dict()
                lista_chaves = [static for static in self.query_one(Grid).query(Static)[
                    1:-6]]
                lista_valores = [input for input in self.query_one(Grid).query(Input)[
                    1:]]

                for chave in lista_chaves:
                    string_limpa = unidecode(chave.content.split()[0].lower())
                    dados[string_limpa] = ""

                for i, valor in enumerate(lista_valores):
                    dados[list(dados.keys())[i]] = valor.value

                atualizacao = Controller.atualizar_item(
                    self.tabela, id_produto, dados)
                self.notify(atualizacao)
                self.limpar_inputs()

            case "Adicionar":
                dados = dict()
                lista_chaves = [static for static in self.query_one(Grid).query(Static)[
                    :-6]]
                lista_valores = [
                    input for input in self.query_one(Grid).query(Input)]

                for chave in lista_chaves:
                    string_limpa = unidecode(chave.content.split()[0].lower())
                    dados[string_limpa] = ""

                for i, valor in enumerate(lista_valores):
                    dados[list(dados.keys())[i]] = valor.value

                adicao = Controller.adicionar_item(self.tabela, dados)
                self.notify(adicao)
                self.limpar_inputs()

            case "Remover":
                id_produto = self.query_one(Input).value
                remocao = Controller.remover_item(self.tabela, id_produto)
                self.notify(remocao)
                self.limpar_inputs()
