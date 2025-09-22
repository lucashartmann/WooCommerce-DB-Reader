from datetime import datetime

class Customers:
    def __init__(self, email):
        self.id = 0  # Unique identifier for the resource.read-only
        # The date the customer was created, in the site's timezone.read-only
        self.date_created: datetime
        # The date the customer was created, as GMT.read-only
        self.date_created_gmt: datetime
        # The date the customer was last modified, in the site's timezone.read-only
        self.date_modified: datetime
        # The date the customer was last modified, as GMT.read-only
        self.date_modified_gmt: datetime
        self.email = email  # The email address for the customer.mandatory
        self.first_name = ""  # Customer first name.
        self.last_name = ""  # Customer last name.
        self.role = ""  # Customer role.read-only
        self.username = ""  # Customer login name.
        self.password = ""  # Customer password.write-only
        self.billing: object  # List of billing address data. See Customer - Billing properties
        self.shipping: object  # List of shipping address data. See Customer - Shipping properties
        self.is_paying_customer = False  # Is the customer a paying customer?read-only
        self.avatar_url = ""  # Avatar URL.read-only
        self.meta_data = []  # Meta data. See Customer - Meta data properties'

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, value):
        self.first_name = value

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, value):
        self.last_name = value

    def get_role(self):
        return self.role

    def set_role(self, value):
        self.role = value

    def get_username(self):
        return self.username

    def set_username(self, value):
        self.username = value

    def get_password(self):
        return self.password

    def set_password(self, value):
        self.password = value

    def get_is_paying_customer(self):
        return self.is_paying_customer

    def set_is_paying_customer(self, value):
        self.is_paying_customer = value

    def get_avatar_url(self):
        return self.avatar_url

    def set_avatar_url(self, value):
        self.avatar_url = value

    def get_meta_data(self):
        return self.meta_data

    def set_meta_data(self, value):
        self.meta_data = value
