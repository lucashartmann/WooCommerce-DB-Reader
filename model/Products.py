class Produto:
    def __init__(self):
        self.name = "" # nome do produto
        self.type = "" # tipo(simple, variable, grouped)
        self.status = "" # status(publish, draft)
        self.regular_price = "" # preço normal
        self.sale_price = "" # preço promocional
        self.description = "" # descrição longa
        self.short_description = "" # descrição curta
        self.sku = "" # código interno
        self.stock_quantity = 0  # quantidade em estoque
        self.manage_stock = False  # controla estoque
        self.categories = list[dict] # lista de categorias [{"id": 15}]
        self.tags = list[dict]  # lista de tags [{"id": 22}]
        self.images = list[dict]  # lista de imagens [{"src": "https://exemplo.com/img.jpg"}]

