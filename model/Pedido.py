class Pedido:
    def __init__(self):
        self.parent_id = 0  # Parent order ID.
        self.created_via = "" # Shows where the order was created. It can only be set during order creation and cannot be modified afterward.
        self.status = "" # Order status. Options: pending, processing, on-hold, completed, cancelled, refunded, failed and trash. Default is pending.
        self.currency = "" # Currency the order was created with, in ISO format. Default is USD.
        self.prices_include_tax = False
        self.customer_id = 0 # User ID who owns the order. 0 for guests. Default is 0.
        self.customer_note = ""  # Note left by customer during checkout.
        self.billing = object  # Billing address. See Order - Billing properties
        self.shipping = object  # Shipping address. See Order - Shipping properties
        self.payment_method = ""  # Payment method ID.
        self.payment_method_title = ""  # Payment method title.
        self.transaction_id = ""  # Unique transaction ID.
        self.meta_data = []  # Meta data. See Order - Meta data properties
        self.line_items = []  # Line items data. See Order - Line items properties
        self.shipping_lines = []  # Shipping lines data. See Order - Shipping lines properties
        self.fee_lines = []  # Fee lines data. See Order - Fee lines properties
        self.coupon_lines = []  # Coupons line data. See Order - Coupon lines properties
        self.set_paid = False  # Define if the

   