from textual.containers import Container, HorizontalGroup
from textual.widgets import Button, TextArea, Input, DataTable
from api import API
from controller import Controller


class TelaConsulta(Container):

    lista_produtos = API.get_lista_produtos()
    lista_produtos_filtrados = []

    ROWS = []

    def compose(self):
        with HorizontalGroup():
            yield Input(placeholder="pesquise aqui")
            yield Button("Remover")
        yield TextArea(read_only=True)
        yield DataTable()

    def on_button_pressed(self):
        id_produto = self.query_one(Input).value
        remocao = Controller.remover_produto(id_produto)
        self.notify(remocao)

    def on_mount(self):
        self.lista_produtos = API.get_lista_produtos()

        quant = len(self.lista_produtos)

        self.query_one(
            TextArea).text = f"Exemplo de busca: 'name: camisa - blusa, id: 1' \n\nQuantidade de lista_produtos: {quant}"

        self.ROWS = []

        lista_chaves = []
        for produto in self.lista_produtos:
            for chave, dados in produto.items():
                if chave and dados and chave not in lista_chaves:
                    lista_chaves.append(chave)
        self.ROWS.append(lista_chaves)

        for produto in self.lista_produtos:
            lista = []
            for valor in produto.values():
                if valor not in lista:
                    lista.append(valor)
            self.ROWS.append(lista)

        table = self.query_one(DataTable)
        for col in self.ROWS[0]:
            table.add_column(col, key=col)
        for row in self.ROWS[1:]:
            table.add_row(*row, height=3)

    def atualizar(self):
        if len(self.lista_produtos_filtrados) > 0:
            lista = self.lista_produtos_filtrados
        else:
            self.lista_produtos = API.get_lista_produtos()
            lista = self.lista_produtos

        self.ROWS = []

        lista_chaves = []
        for produto in lista:
            for chave, dados in produto.items():
                if chave and dados and chave not in lista_chaves:
                    lista_chaves.append(chave)
        self.ROWS.append(lista_chaves)

        for produto in lista:
            lista = []
            for valor in produto.values():
                if valor not in lista:
                    lista.append(valor)
            self.ROWS.append(lista)

        table = self.query_one(DataTable)
        table.clear(columns=True)

        for col in self.ROWS[0]:
            table.add_column(col, key=col)
        for row in self.ROWS[1:]:
            table.add_row(*row, height=3)

    def filtro(self, palavras, index, filtro_recebido):
        lista_filtros = ["id", "price"]
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

        if len(palavras) > 0:
            self.lista_produtos_filtrados = []

            for palavra in palavras:
                match palavra:
                    case  "NAME:" | "name:":
                        try:
                            index = palavras.index("NAME:")
                        except:
                            index = palavras.index("name:")
                        self.filtro(palavras, index, "name")

                    case "ID:" | "id:":
                        try:
                            index = palavras.index("ID:")
                        except:
                            index = palavras.index("id:")
                        self.filtro(palavras, index, "id")

                    case "PRICE" | "price:":
                        try:
                            index = palavras.index("PRICE:")
                        except:
                            index = palavras.index("price:")
                        self.filtro(palavras, index, "price")

                self.atualizar()
        else:
            self.atualizar()
