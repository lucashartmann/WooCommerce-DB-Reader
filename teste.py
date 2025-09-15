from model import Produto

um_produto = Produto.Produto()

for chave, valor in um_produto.__dict__.items():
    print(f"{chave}: {valor}", end="\n")
