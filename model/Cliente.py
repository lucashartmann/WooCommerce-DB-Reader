from datetime import datetime

class Customers:
    def __init__(self):
        self.id	= 0	# Unique identifier for the resource.read-only
        self.date_created:datetime	# The date the customer was created, in the site's timezone.read-only
        self.date_created_gmt:datetime	# The date the customer was created, as GMT.read-only
        self.date_modified:datetime	# The date the customer was last modified, in the site's timezone.read-only
        self.date_modified_gmt:datetime	# The date the customer was last modified, as GMT.read-only
        self.email = ""	# The email address for the customer.mandatory
        self.first_name	= ""	# Customer first name.
        self.last_name = ""	# Customer last name.
        self.role = ""	# Customer role.read-only
        self.username = ""	# Customer login name.
        self.password = ""	# Customer password.write-only
        self.billing:object	# List of billing address data. See Customer - Billing properties
        self.shipping:object	# List of shipping address data. See Customer - Shipping properties
        self.is_paying_customer = False	# Is the customer a paying customer?read-only
        self.avatar_url	= ""	# Avatar URL.read-only
        self.meta_data = []# Meta data. See Customer - Meta data properties'