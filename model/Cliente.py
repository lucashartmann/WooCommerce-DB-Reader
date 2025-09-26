class Cliente:
    def __init__(self, email:str):
        self.email = email  # The email address for the customer.mandatory
        self.first_name = ""  # Customer first name.
        self.last_name = ""  # Customer last name.
        self.username = ""  # Customer login name.
        self.password = ""  # Customer password.write-only
        self.billing = object  # List of billing address data. See Customer - Billing properties
        self.shipping = object  # List of shipping address data. See Customer - Shipping properties
        self.meta_data = []  # Meta data. See Customer - Meta data properties'
