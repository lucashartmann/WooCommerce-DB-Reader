from textual.screen import Screen
from textual.widgets import Button, TextArea, Header, Footer
from textual.containers import HorizontalGroup
from api import API
from database import Shelve


class TelaInicial(Screen):

    CSS_PATH = "css/TelaInicial.tcss"

    def compose(self):
        # yield Input()
        yield Header()
        with HorizontalGroup():
            yield Button("Adicionar", id="bt_adicionar")
            yield Button("Consultar", id="bt_consultar")
        yield TextArea(read_only=True)
        yield Footer()

    def on_button_pressed(self, evento: Button.Pressed):
        ta = self.query_one(TextArea)

        match evento.button.id:
            case "bt_adicionar":
                ta.text = API.adicionar()
            case "bt_consultar":
                lista = API.get_lista_produtos()
                resultado = ""
                for produto in lista:
                    for chave, valor in produto.items():
                        if valor and chave:
                            resultado += f"{chave}: {valor} \n"
                ta.text = resultado
