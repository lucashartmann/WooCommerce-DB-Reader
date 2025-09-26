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
        self.date_on_sale_from = datetime(2025,1,1) #	Start date of sale price, in the site's timezone.
        self.date_on_sale_from_gmt = datetime(2025,1,1) #	Start date of sale price, as GMT.
        self.date_on_sale_to = datetime(2025,1,1) #	End date of sale price, in the site's timezone.
        self.date_on_sale_to_gmt = datetime(2025,1,1) #	End date of sale price, as GMT.
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

   