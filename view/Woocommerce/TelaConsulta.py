from textual.containers import HorizontalGroup
from textual.widgets import Button, TextArea, Input, DataTable, Select, Tabs, Tab
from api import API
from controller import Controller
from textual.screen import Screen


class TelaConsulta(Screen):

    CSS_PATH = "css/TelaConsulta.tcss"

    lista_produtos = []
    lista_produtos_filtrados = []
    tabela = "products"
    ROWS = []

    filtros_tabela = {
        "products": ["id", "name", "price", "description"],
        "customers": ["id", "email", "first_name", "last_name"],
        "orders": ["id", "customer_id"],
        "coupons": ["id", "code", "amount", "date_expires"]
    }

    def compose(self):
        with HorizontalGroup():
            yield Tabs(Tab("TelaCadastrar"), Tab("TelaConsultar", id="tab_Consultar"))
            yield Select([("Products", "Products"), ("Orders", "Orders"), ("Customers", "Customers"), ("Coupons", "Coupons")], allow_blank=False)
            yield Input(placeholder="pesquise aqui")
            yield Button("Remover")
        yield TextArea(read_only=True)
        yield DataTable()

    def on_button_pressed(self):
        id_produto = self.query_one(Input).value
        remocao = Controller.remover_item(self.tabela, id_produto)
        self.notify(remocao)
        self.atualizar()
        for input in self.query(Input):
            input.value = ""

    def on_tabs_tab_activated(self, event: Tabs.TabActivated):
        if event.tab.label == "TelaCadastrar":
            self.app.switch_screen("tela_cadastro")

    def on_select_changed(self, evento: Select.Changed):
        match evento.select.value:
            case "Products":
                self.tabela = "products"
            case "Customers":
                self.tabela = "customers"
            case "Coupons":
                self.tabela = "coupons"
            case "Orders":
                self.tabela = "orders"
        self.atualizar()

    def on_mount(self):
        Tabs.focus(self.query_one("#tab_Consultar", Tab))
        self.atualizar()

    def atualizar(self):
        if len(self.lista_produtos_filtrados) > 0:
            lista = self.lista_produtos_filtrados
        else:
            self.lista_produtos = API.get_lista_itens(self.tabela)
            lista = self.lista_produtos

        quant = len(self.lista_produtos)

        self.query_one(
            TextArea).text = f"Exemplo de busca: 'name: camisa - blusa, id: 1' \n\nQuantidade de itens: {quant}"

        self.ROWS = []

        lista_chaves = []
        for produto in lista:
            for chave, dados in produto.items():
                if dados and chave not in lista_chaves and chave in self.filtros_tabela[self.tabela]:
                    lista_chaves.append(chave)
        self.ROWS.append(lista_chaves)

        for produto in lista:
            lista = []
            for chave, valor in produto.items():
                if valor and valor not in lista and chave in self.filtros_tabela[self.tabela]:
                    lista.append(valor)
            self.ROWS.append(lista)

        table = self.query_one(DataTable)
        table.clear(columns=True)

        table.add_columns(*self.ROWS[0])

        for row in self.ROWS[1:]:
            table.add_row(*row, height=3)

    def filtro(self, palavras, index, filtro_recebido):
        lista_filtros = ["id", "customer_id"]
        nova_lista = []

        if index + 1 < len(palavras):
            filtro = " ".join((palavras[index+1:]))

            if "," in filtro:
                filtro = filtro[0:filtro.index(
                    ",")]
            if "-" in filtro.split():
                for palavraa in filtro.split("-"):
                    if filtro.index("-")+1 < len(filtro) and palavraa not in nova_lista:
                        nova_lista.append(palavraa.strip())

            if filtro_recebido in lista_filtros:
                try:
                    filtro = int(filtro)
                except ValueError:
                    self.notify("Valor Inválido")
                    return

            if len(self.lista_produtos_filtrados) > 0:
                produtos_temp = []
                if len(nova_lista) > 0:
                    for p in nova_lista:
                        for produto in self.lista_produtos_filtrados:
                            if type(filtro) == int:
                                if p == produto[filtro_recebido] and produto not in produtos_temp:
                                    produtos_temp.append(
                                        produto)
                            else:
                                if p in produto[filtro_recebido] and produto not in produtos_temp:
                                    produtos_temp.append(
                                        produto)
                else:
                    for produto in self.lista_produtos_filtrados:
                        if type(filtro) == int:
                            if filtro == produto[filtro_recebido] and produto not in produtos_temp:
                                produtos_temp.append(produto)
                        else:
                            if filtro in produto[filtro_recebido] and produto not in produtos_temp:
                                produtos_temp.append(produto)
                if len(produtos_temp) > 0:
                    self.lista_produtos_filtrados = produtos_temp
            else:
                if len(nova_lista) > 0:
                    for p in nova_lista:
                        for produto in self.lista_produtos:
                            if type(filtro) == int:
                                if p == produto[filtro_recebido] and produto not in self.lista_produtos_filtrados:
                                    self.lista_produtos_filtrados.append(
                                        produto)
                            else:
                                if p in produto[filtro_recebido] and produto not in self.lista_produtos_filtrados:
                                    self.lista_produtos_filtrados.append(
                                        produto)
                else:
                    for produto in self.lista_produtos:
                        if type(filtro) == int:
                            if filtro == produto[filtro_recebido] and produto not in self.lista_produtos_filtrados:
                                self.lista_produtos_filtrados.append(produto)
                        else:
                            if filtro in produto[filtro_recebido] and produto not in self.lista_produtos_filtrados:
                                self.lista_produtos_filtrados.append(produto)

    def on_input_changed(self, evento: Input.Changed):
        texto = evento.value
        palavras = texto.split()
        lista = ["name:", "id:", "price:", "description:", "email:",
                 "first_name", "last_name", "code", "amount", "date_expires"]

        if len(palavras) > 0:
            self.lista_produtos_filtrados = []
            for palavra in palavras:
                if palavra.lower() in lista:
                    index = palavras.index(palavra)
                    self.filtro(palavras, index, palavra[:-1].lower())
                    self.atualizar()
        else:
            self.atualizar()
