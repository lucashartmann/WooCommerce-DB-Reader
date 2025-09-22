from datetime import datetime

class Coupons:
    def __init__(self, code):
        self.id = 0  # Unique identifier for the object.read-only
        self.code = code  # Coupon code.mandatory
        # The amount of discount. Should always be numeric, even if setting a percentage.
        self.amount = ""
        # The date the coupon was created, in the site's timezone.read-only
        self.date_create: datetime
        self.date_created_gmt: datetime  # The date the coupon was created, as GMT.read-only
        # The date the coupon was last modified, in the site's timezone.read-only
        self.date_modified: datetime
        # The date the coupon was last modified, as GMT.read-only
        self.date_modified_gmt: datetime
        # Determines the type of discount that will be applied. Options: percent, fixed_cart and fixed_product. Default is fixed_cart.
        self.discount_type = ""
        self.description = ""  # Coupon description.
        # The date the coupon expires, in the site's timezone.
        self.date_expires = ""
        self.date_expires_gmt = ""  # The date the coupon expires, as GMT.
        self.usage_count = 0  # Number of times the coupon has been used already.read-only
        # If true, the coupon can only be used individually. Other applied coupons will be removed from the cart. Default is false.
        self.individual_use = False
        self.product_ids = []  # List of product IDs the coupon can be used on.
        # List of product IDs the coupon cannot be used on.
        self.excluded_product_ids = []
        self.usage_limit = 0  # How many times the coupon can be used in total.
        # How many times the coupon can be used per customer.
        self.usage_limit_per_user = 0
        # Max number of items in the cart the coupon can be applied to.
        self.limit_usage_to_x_items = 0
        # If true and if the free shipping method requires a coupon, this coupon will enable free shipping. Default is false.
        self.free_shipping = False
        # List of category IDs the coupon applies to.
        self.product_categories = []
        # List of category IDs the coupon does not apply to.
        self.excluded_product_categories = []
        # If true, this coupon will not be applied to items that have sale prices. Default is false.
        self.exclude_sale_items = False
        # Minimum order amount that needs to be in the cart before coupon applies.
        self.minimum_amount = ""
        # Maximum order amount allowed when using the coupon.
        self.maximum_amount = ""
        # List of email addresses that can use this coupon.
        self.email_restrictions = []
        # List of user IDs (or guest email addresses) that have used the coupon.read-only
        self.used_by = []
        self.meta_data = []  # Meta data. See Coupon - Meta data properties

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_code(self):
        return self.code

    def set_code(self, value):
        self.code = value

    def get_amount(self):
        return self.amount

    def set_amount(self, value):
        self.amount = value

    def get_discount_type(self):
        return self.discount_type

    def set_discount_type(self, value):
        self.discount_type = value

    def get_description(self):
        return self.description

    def set_description(self, value):
        self.description = value

    def get_date_expires(self):
        return self.date_expires

    def set_date_expires(self, value):
        self.date_expires = value

    def get_date_expires_gmt(self):
        return self.date_expires_gmt

    def set_date_expires_gmt(self, value):
        self.date_expires_gmt = value

    def get_usage_count(self):
        return self.usage_count

    def set_usage_count(self, value):
        self.usage_count = value

    def get_individual_use(self):
        return self.individual_use

    def set_individual_use(self, value):
        self.individual_use = value

    def get_product_ids(self):
        return self.product_ids

    def set_product_ids(self, value):
        self.product_ids = value

    def get_excluded_product_ids(self):
        return self.excluded_product_ids

    def set_excluded_product_ids(self, value):
        self.excluded_product_ids = value

    def get_usage_limit(self):
        return self.usage_limit

    def set_usage_limit(self, value):
        self.usage_limit = value

    def get_usage_limit_per_user(self):
        return self.usage_limit_per_user

    def set_usage_limit_per_user(self, value):
        self.usage_limit_per_user = value

    def get_limit_usage_to_x_items(self):
        return self.limit_usage_to_x_items

    def set_limit_usage_to_x_items(self, value):
        self.limit_usage_to_x_items = value

    def get_free_shipping(self):
        return self.free_shipping

    def set_free_shipping(self, value):
        self.free_shipping = value

    def get_product_categories(self):
        return self.product_categories

    def set_product_categories(self, value):
        self.product_categories = value

    def get_excluded_product_categories(self):
        return self.excluded_product_categories

    def set_excluded_product_categories(self, value):
        self.excluded_product_categories = value

    def get_exclude_sale_items(self):
        return self.exclude_sale_items

    def set_exclude_sale_items(self, value):
        self.exclude_sale_items = value

    def get_minimum_amount(self):
        return self.minimum_amount

    def set_minimum_amount(self, value):
        self.minimum_amount = value

    def get_maximum_amount(self):
        return self.maximum_amount

    def set_maximum_amount(self, value):
        self.maximum_amount = value

    def get_email_restrictions(self):
        return self.email_restrictions

    def set_email_restrictions(self, value):
        self.email_restrictions = value

    def get_used_by(self):
        return self.used_by

    def set_used_by(self, value):
        self.used_by = value

    def get_meta_data(self):
        return self.meta_data

    def set_meta_data(self, value):
        self.meta_data = value
