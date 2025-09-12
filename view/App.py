from textual.app import App
from view import TelaLogin, TelaInicial
from database import Shelve
from api import API


class App(App):

    SCREENS = {
        "tela_login": TelaLogin.Login,
        "tela_inicial": TelaInicial.TelaInicial
    }

    def on_mount(self):
        dados = Shelve.carregar("dados.db", "login")
        if dados:
            API.wcapi.url = dados[0]
            API.wcapi.consumer_key = dados[1]
            API.wcapi.consumer_secret = dados[2]
            self.push_screen("tela_inicial")
        else:
            self.push_screen("tela_login")
