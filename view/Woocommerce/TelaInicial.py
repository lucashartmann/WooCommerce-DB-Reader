from textual.screen import Screen
from textual.widgets import Header, Footer, TabPane, TabbedContent
from view.Woocommerce import TelaCadastro, TelaConsulta

class TelaInicial(Screen):

    CSS_PATH = "css/TelaInicial.tcss"

    def compose(self):
        yield Header()
        with TabbedContent():
            with TabPane("Cadastrar"):
                yield TelaCadastro.TelaCadastro()
            with TabPane("Consultar"):
                yield TelaConsulta.TelaConsulta()
        yield Footer()


    def on_cadastro_realizado(self):
        tela_consulta = self.query_one(TelaConsulta.TelaConsulta)
        tela_consulta.atualizar()
