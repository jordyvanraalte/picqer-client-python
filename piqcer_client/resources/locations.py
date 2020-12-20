from ..resources.resource import Resource
import requests
from requests.auth import HTTPBasicAuth


class Locations(Resource):
    def __init__(self):
        super().__init__("locations")

    def get_products_on_location(self, id):
        return requests.get(self.config.base_url + self.path + '/' + str(id) + "/products",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

