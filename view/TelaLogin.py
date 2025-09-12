from textual.screen import Screen
from textual.widgets import Label, Input, Button
from api import API
from database import Shelve


class Login(Screen):

    CSS_PATH = "css/TelaLogin.tcss"

    def compose(self):
        yield Input(placeholder="url")
        yield Input(placeholder="consumer_key")
        yield Input(placeholder="cosumer_secret")
        yield Button("Entrar")

    def on_button_pressed(self):
        dados = []
        for input in self.query(Input):
            dados.append(input.value)
        API.wcapi.url = dados[0]
        API.wcapi.consumer_key = dados[1]
        API.wcapi.consumer_secret = dados[2]
        Shelve.salvar("dados.db", "login", dados)
        self.app.switch_screen("tela_inicial")
