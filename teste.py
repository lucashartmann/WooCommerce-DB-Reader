from database import Shelve
from model import Produto

um_produto = Produto.Produto()

for i, name in enumerate(um_produto.__dict__.keys()):
     print(f"{name}:{i}")

