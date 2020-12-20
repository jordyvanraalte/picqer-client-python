import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Receipts(Resource):
    def __init__(self):
        super().__init__("receipts")

    def mark_all_received(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/mark-all-received", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def scan_product(self, id, product_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/products", data=product_object, verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def add_product(self, id, product_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/products?force=true", data=product_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def change_amount_or_location(self, id, id_product, change_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/products/" + str(id_product),
                             data=change_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()