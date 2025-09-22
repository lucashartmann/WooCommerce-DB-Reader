from database import Shelve
from model import Produto

um_produto = Produto.Produto()

for chave, valor in um_produto.__dict__.items():
    if valor:
        print(f"{chave}:{valor}")

