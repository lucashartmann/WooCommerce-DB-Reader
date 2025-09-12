from textual.screen import Screen
from textual.widgets import Label, Input, Button
from api import API
from database import Shelve


class TelaInicial(Screen):

    CSS_PATH = "css/TelaInicial.tcss"

    def compose(self):
        yield Input()

    def on_mount(self):
        self.notify(str(API.adicionar()))
