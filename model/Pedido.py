from datetime import datetime

class Pedido:
    def __init__(self):
        self.parent_id = 0  # Parent order ID.
        # Shows where the order was created. It can only be set during order creation and cannot be modified afterward.
        self.created_via = ""
        # Order status. Options: pending, processing, on-hold, completed, cancelled, refunded, failed and trash. Default is pending.
        self.status = ""
        # Currency the order was created with, in ISO format. Default is USD.
        self.currency = ""
        self.prices_include_tax = False
        # User ID who owns the order. 0 for guests. Default is 0.
        self.customer_id = 0
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

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_parent_id(self):
        return self.parent_id

    def set_parent_id(self, value):
        self.parent_id = value

    def get_number(self):
        return self.number

    def set_number(self, value):
        self.number = value

    def get_order_key(self):
        return self.order_key

    def set_order_key(self, value):
        self.order_key = value

    def get_created_via(self):
        return self.created_via

    def set_created_via(self, value):
        self.created_via = value

    def get_version(self):
        return self.version

    def set_version(self, value):
        self.version = value

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_currency(self):
        return self.currency

    def set_currency(self, value):
        self.currency = value

    def get_discount_total(self):
        return self.discount_total

    def set_discount_total(self, value):
        self.discount_total = value

    def get_discount_tax(self):
        return self.discount_tax

    def set_discount_tax(self, value):
        self.discount_tax = value

    def get_shipping_total(self):
        return self.shipping_total

    def set_shipping_total(self, value):
        self.shipping_total = value

    def get_shipping_tax(self):
        return self.shipping_tax

    def set_shipping_tax(self, value):
        self.shipping_tax = value

    def get_cart_tax(self):
        return self.cart_tax

    def set_cart_tax(self, value):
        self.cart_tax = value

    def get_total(self):
        return self.total

    def set_total(self, value):
        self.total = value

    def get_total_tax(self):
        return self.total_tax

    def set_total_tax(self, value):
        self.total_tax = value

    def get_prices_include_tax(self):
        return self.prices_include_tax

    def set_prices_include_tax(self, value):
        self.prices_include_tax = value

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, value):
        self.customer_id = value

    def get_customer_ip_address(self):
        return self.customer_ip_address

    def set_customer_ip_address(self, value):
        self.customer_ip_address = value

    def get_customer_user_agent(self):
        return self.customer_user_agent

    def set_customer_user_agent(self, value):
        self.customer_user_agent = value

    def get_customer_note(self):
        return self.customer_note

    def set_customer_note(self, value):
        self.customer_note = value

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, value):
        self.payment_method = value

    def get_payment_method_title(self):
        return self.payment_method_title

    def set_payment_method_title(self, value):
        self.payment_method_title = value

    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_id(self, value):
        self.transaction_id = value

    def get_cart_hash(self):
        return self.cart_hash

    def set_cart_hash(self, value):
        self.cart_hash = value

    def get_meta_data(self):
        return self.meta_data

    def set_meta_data(self, value):
        self.meta_data = value

    def get_line_items(self):
        return self.line_items

    def set_line_items(self, value):
        self.line_items = value

    def get_tax_lines(self):
        return self.tax_lines

    def set_tax_lines(self, value):
        self.tax_lines = value

    def get_shipping_lines(self):
        return self.shipping_lines

    def set_shipping_lines(self, value):
        self.shipping_lines = value

    def get_fee_lines(self):
        return self.fee_lines

    def set_fee_lines(self, value):
        self.fee_lines = value

    def get_coupon_lines(self):
        return self.coupon_lines

    def set_coupon_lines(self, value):
        self.coupon_lines = value

    def get_refunds(self):
        return self.refunds

    def set_refunds(self, value):
        self.refunds = value

    def get_set_paid(self):
        return self.set_paid

    def set_set_paid(self, value):
        self.set_paid = value
