from datetime import datetime

class Produto:
    def __init__(self):
        self.name	= "" #	Product name.
        self.slug	= "" #	Product slug.
        self.type	= "" #	Product type. Options: simple, grouped, external and variable. Default is simple.
        self.status	= "" #	Product status (post status). Options: draft, pending, private and publish. Default is publish.
        self.featured	= False #	Featured product. Default is false.
        self.catalog_visibility	= "" #	Catalog visibility. Options: visible, catalog, search and hidden. Default is visible.
        self.description	= "" #	Product description.
        self.short_description	= "" #	Product short description.
        self.sku	= "" #	Unique identifier.
        self.global_unique_id	= "" #	GTIN, UPC, EAN or ISBN - a unique identifier for each distinct product and service that can be purchased.
        self.regular_price	= "" #	Product regular price.
        self.sale_price	= "" #	Product sale price.
        self.date_on_sale_from = datetime #	Start date of sale price, in the site's timezone.
        self.date_on_sale_from_gmt = datetime #	Start date of sale price, as GMT.
        self.date_on_sale_to = datetime #	End date of sale price, in the site's timezone.
        self.date_on_sale_to_gmt = datetime #	End date of sale price, as GMT.
        self.virtual	= False #	If the product is virtual. Default is false.
        self.downloadable	= False #	If the product is downloadable. Default is false.
        self.downloads = [] #	List of downloadable files. See Product - Downloads properties
        self.download_limit	= 0 #	Number of times downloadable files can be downloaded after purchase. Default is -1.
        self.download_expiry	= 0 #	Number of days until access to downloadable files expires. Default is -1.
        self.external_url	= "" #	Product external URL. Only for external products.
        self.button_text	= "" #	Product external button text. Only for external products.
        self.tax_status	= "" #	Tax status. Options: taxable, shipping and none. Default is taxable.
        self.tax_class	= "" #	Tax class.
        self.manage_stock	= False #	Stock management at product level. Default is false.
        self.stock_quantity	= 0 #	Stock quantity.
        self.stock_status	= "" #	Controls the stock status of the product. Options: instock, outofstock, onbackorder. Default is instock.
        self.backorders	= "" #	If managing stock, this controls if backorders are allowed. Options: no, notify and yes. Default is no.
        self.sold_individually	= False #	Allow one item to be bought in a single order. Default is false.
        self.weight	= "" #	Product weight.
        self.dimensions:object	# Product dimensions. See Product - Dimensions properties
        self.shipping_class	= "" #	Shipping class slug.
        self.reviews_allowed	= False #	Allow reviews. Default is true.
        self.upsell_ids = [] #	List of up-sell products IDs.
        self.cross_sell_ids = [] #	List of cross-sell products IDs.
        self.parent_id	= 0 #	Product parent ID.
        self.purchase_note	= "" #	Optional note to send the customer after purchase.
        self.categories = [] #	List of categories. See Product - Categories properties
        self.tags = [] #	List of tags. See Product - Tags properties
        self.images = [] #	List of images. See Product - Images properties
        self.attributes = [] #	List of attributes. See Product - Attributes properties
        self.default_attributes = [] #	Defaults variation attributes. See Product - Default attributes properties
        self.grouped_products = [] #	List of grouped products ID.
        self.menu_order	= 0 #	Menu order, used to custom sort products.
        self.meta_data = [] #	Meta data. See Product - Meta data properties

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_slug(self):
        return self.slug

    def set_slug(self, value):
        self.slug = value

    def get_permalink(self):
        return self.permalink

    def set_permalink(self, value):
        self.permalink = value

    def get_type(self):
        return self.type

    def set_type(self, value):
        self.type = value

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_featured(self):
        return self.featured

    def set_featured(self, value):
        self.featured = value

    def get_catalog_visibility(self):
        return self.catalog_visibility

    def set_catalog_visibility(self, value):
        self.catalog_visibility = value

    def get_description(self):
        return self.description

    def set_description(self, value):
        self.description = value

    def get_short_description(self):
        return self.short_description

    def set_short_description(self, value):
        self.short_description = value

    def get_sku(self):
        return self.sku

    def set_sku(self, value):
        self.sku = value

    def get_global_unique_id(self):
        return self.global_unique_id

    def set_global_unique_id(self, value):
        self.global_unique_id = value

    def get_price(self):
        return self.price

    def set_price(self, value):
        self.price = value

    def get_regular_price(self):
        return self.regular_price

    def set_regular_price(self, value):
        self.regular_price = value

    def get_sale_price(self):
        return self.sale_price

    def set_sale_price(self, value):
        self.sale_price = value

    def get_price_html(self):
        return self.price_html

    def set_price_html(self, value):
        self.price_html = value

    def get_on_sale(self):
        return self.on_sale

    def set_on_sale(self, value):
        self.on_sale = value

    def get_purchasable(self):
        return self.purchasable

    def set_purchasable(self, value):
        self.purchasable = value

    def get_total_sales(self):
        return self.total_sales

    def set_total_sales(self, value):
        self.total_sales = value

    def get_virtual(self):
        return self.virtual

    def set_virtual(self, value):
        self.virtual = value

    def get_downloadable(self):
        return self.downloadable

    def set_downloadable(self, value):
        self.downloadable = value

    def get_downloads(self):
        return self.downloads

    def set_downloads(self, value):
        self.downloads = value

    def get_download_limit(self):
        return self.download_limit

    def set_download_limit(self, value):
        self.download_limit = value

    def get_download_expiry(self):
        return self.download_expiry

    def set_download_expiry(self, value):
        self.download_expiry = value

    def get_external_url(self):
        return self.external_url

    def set_external_url(self, value):
        self.external_url = value

    def get_button_text(self):
        return self.button_text

    def set_button_text(self, value):
        self.button_text = value

    def get_tax_status(self):
        return self.tax_status

    def set_tax_status(self, value):
        self.tax_status = value

    def get_tax_class(self):
        return self.tax_class

    def set_tax_class(self, value):
        self.tax_class = value

    def get_manage_stock(self):
        return self.manage_stock

    def set_manage_stock(self, value):
        self.manage_stock = value

    def get_stock_quantity(self):
        return self.stock_quantity

    def set_stock_quantity(self, value):
        self.stock_quantity = value

    def get_stock_status(self):
        return self.stock_status

    def set_stock_status(self, value):
        self.stock_status = value

    def get_backorders(self):
        return self.backorders

    def set_backorders(self, value):
        self.backorders = value

    def get_backorders_allowed(self):
        return self.backorders_allowed

    def set_backorders_allowed(self, value):
        self.backorders_allowed = value

    def get_backordered(self):
        return self.backordered

    def set_backordered(self, value):
        self.backordered = value

    def get_sold_individually(self):
        return self.sold_individually

    def set_sold_individually(self, value):
        self.sold_individually = value

    def get_weight(self):
        return self.weight

    def set_weight(self, value):
        self.weight = value

    def get_shipping_required(self):
        return self.shipping_required

    def set_shipping_required(self, value):
        self.shipping_required = value

    def get_shipping_taxable(self):
        return self.shipping_taxable

    def set_shipping_taxable(self, value):
        self.shipping_taxable = value

    def get_shipping_class(self):
        return self.shipping_class

    def set_shipping_class(self, value):
        self.shipping_class = value

    def get_shipping_class_id(self):
        return self.shipping_class_id

    def set_shipping_class_id(self, value):
        self.shipping_class_id = value

    def get_reviews_allowed(self):
        return self.reviews_allowed

    def set_reviews_allowed(self, value):
        self.reviews_allowed = value

    def get_average_rating(self):
        return self.average_rating

    def set_average_rating(self, value):
        self.average_rating = value

    def get_rating_count(self):
        return self.rating_count

    def set_rating_count(self, value):
        self.rating_count = value

    def get_related_ids(self):
        return self.related_ids

    def set_related_ids(self, value):
        self.related_ids = value

    def get_upsell_ids(self):
        return self.upsell_ids

    def set_upsell_ids(self, value):
        self.upsell_ids = value

    def get_cross_sell_ids(self):
        return self.cross_sell_ids

    def set_cross_sell_ids(self, value):
        self.cross_sell_ids = value

    def get_parent_id(self):
        return self.parent_id

    def set_parent_id(self, value):
        self.parent_id = value

    def get_purchase_note(self):
        return self.purchase_note

    def set_purchase_note(self, value):
        self.purchase_note = value

    def get_categories(self):
        return self.categories

    def set_categories(self, value):
        self.categories = value

    def get_tags(self):
        return self.tags

    def set_tags(self, value):
        self.tags = value

    def get_images(self):
        return self.images

    def set_images(self, value):
        self.images = value

    def get_attributes(self):
        return self.attributes

    def set_attributes(self, value):
        self.attributes = value

    def get_default_attributes(self):
        return self.default_attributes

    def set_default_attributes(self, value):
        self.default_attributes = value

    def get_variations(self):
        return self.variations

    def set_variations(self, value):
        self.variations = value

    def get_grouped_products(self):
        return self.grouped_products

    def set_grouped_products(self, value):
        self.grouped_products = value

    def get_menu_order(self):
        return self.menu_order

    def set_menu_order(self, value):
        self.menu_order = value

    def get_meta_data(self):
        return self.meta_data

    def set_meta_data(self, value):
        self.meta_data = value
