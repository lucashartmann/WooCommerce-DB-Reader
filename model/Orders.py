class Oders:
    def __init__(self):
        self.status = ""  # status inicial (pending, processing, etc.)
        self.currency = "BRL" 
        self.customer_id = 0  # id do cliente 
        self.billing = dict()  # dados de cobrança (nome, email, endereço, etc.)
        self.shipping = dict() # dados de entrega
        self.line_items = list[dict] # lista de produtos (product_id, quantity, total)
        self.shipping_lines = list[dict] # informações de frete