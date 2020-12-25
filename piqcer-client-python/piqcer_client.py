from .config.config import Config
from .resources.backorders import Backorders
from .resources.customer_fields import CustomerFields
from .resources.customers import Customers
from .resources.locations import Locations
from .resources.order_fields import OrderFields
from .resources.orders import Orders
from .resources.picklists import Picklists
from .resources.pricelists import PriceLists
from .resources.product_fields import ProductFields
from .resources.products import Products
from .resources.purchase_orders import PurchaseOrders
from .resources.receipts import Receipts
from .resources.returns import Returns
from .resources.shipping_provider import ShippingProviders
from .resources.stock_history import StockHistory
from .resources.suppliers import Suppliers
from .resources.tags import Tags
from .resources.users import Users
from .resources.vat_group import VatGroup
from .resources.warehouses import Warehouses


class Client:

    def __init__(self, api_key, base_url):
        config = Config()
        config.base_url = base_url
        config.api_key = api_key

        self.backorders = Backorders()
        self.customer_fields = CustomerFields()
        self.customers = Customers()
        self.locations = Locations()
        self.order_fields = OrderFields()
        self.orders = Orders()
        self.picklists = Picklists()
        self.pricelists = PriceLists()
        self.product_fields = ProductFields()
        self.products = Products()
        self.purchase_orders = PurchaseOrders()
        self.receipts = Receipts()
        self.returns = Returns()
        self.shipping_provider = ShippingProviders()
        self.stock_history = StockHistory()
        self.suppliers = Suppliers()
        self.tags = Tags()
        self.users = Users()
        self.vat_group = VatGroup()
        self.warehouses = Warehouses()
