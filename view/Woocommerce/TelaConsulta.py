from textual.containers import Container, HorizontalGroup
from textual.widgets import Button, TextArea, Input, DataTable
from api import API


class TelaConsulta(Container):

    lista_produtos = API.get_lista_produtos()
    lista_produtos_filtrados = []

    ROWS = []

    def compose(self):
        with HorizontalGroup():
            yield Input(placeholder="pesquise aqui")
            yield Button("Consultar", id="bt_consultar")
        yield TextArea(read_only=True, id="tx_info")
        yield DataTable()

    def on_mount(self):
        self.lista_produtos = API.get_lista_produtos()

        quant = len(self.lista_produtos)

        self.query_one(
            "#tx_info", TextArea).text = f"Exemplo de busca: 'titulo: Maus - 1984, genero: distopia' \n\nQuantidade de lista_produtos: {quant}"

        self.ROWS = [self.lista_produtos[0].keys()]

        for produto in self.lista_produtos:
            lista = []
            for valor in produto.values():
                if valor not in lista:
                    lista.append(valor)
            self.ROWS.append(lista)

        table = self.query_one(DataTable)
        for col in self.ROWS[0]:
            table.add_column(col, key=col)
        table.add_rows(self.ROWS[1:])

    def atualizar(self):
        if len(self.lista_produtos_filtrados) > 0:
            lista = self.lista_produtos_filtrados
        else:
            self.lista_produtos = API.get_lista_produtos()
            lista = self.lista_produtos

        self.ROWS = []
        self.ROWS = [self.lista_produtos[0].keys()]

        for produto in lista:
            lista = []
            for valor in produto.values():
                if valor not in lista:
                    lista.append(valor)
            self.ROWS.append(lista)

        table = self.query_one(DataTable)
        table.clear()
        table.add_rows(self.ROWS[1:])

    def filtro(self, palavras, index, filtro_recebido):
        lista_filtros = ["id"]
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
        texto = evento.value.upper()
        palavras = texto.split()

        if len(palavras) > 0:
            self.lista_produtos_filtrados = []

            for palavra in palavras:
                match palavra:
                    case  "NAME:":
                        index = palavras.index("NAME:")
                        self.filtro(palavras, index, "name")

                    case "ID:":
                        index = palavras.index("ID:")
                        self.filtro(palavras, index, "id")

                self.atualizar()
        else:
            self.atualizar()
