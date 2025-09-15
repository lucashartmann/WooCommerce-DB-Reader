from textual.containers import Container, HorizontalGroup
from textual.widgets import Button, TextArea
from api import API

class TelaCadastro(Container): 

    def compose(self):
        with HorizontalGroup():
            yield Button("Adicionar", id="bt_adicionar")
        yield TextArea(read_only=True)

    def on_button_pressed(self, evento: Button.Pressed):
        ta = self.query_one(TextArea)

        match evento.button.id:
            case "bt_adicionar":
                ta.text = API.adicionar2()
            