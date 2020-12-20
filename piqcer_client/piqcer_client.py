from .config.config import Config
from .resources.users import Users
from .resources.customers import Customers


class Client:

    def __init__(self, api_key, base_url):
        config = Config()
        config.base_url = base_url
        config.api_key = api_key

        self.users = Users()
        self.customers = Customers()
