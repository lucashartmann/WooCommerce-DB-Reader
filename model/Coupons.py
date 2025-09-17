class Coupons:
    def __init__(self):
        self.code = "" # código do cupom
        self.discount_type = "" # tipo (fixed_cart, percent, fixed_product)
        self.amount = "" # valor do desconto
        self.date_expires = "" # validade
        self.usage_limit = 0 # limite de uso
        self.individual_use = False # se pode ser usado junto com outros cupons (true/false)