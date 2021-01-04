import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class PurchaseOrders(Resource):
    def __init__(self):
        super().__init__("purchaseorders")

    def mark_as_purchased(self, id):
        return requests.post(self.config.base_url + self.path + '/' + str(id) + "/mark-as-purchased",
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def cancel(self, id):
        return requests.post(self.config.base_url + self.path + '/' + str(id) + "/cancel",
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_all_products(self, id):
        return requests.get(self.config.base_url + self.path + '/' + str(id) + "/products", verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_all_products_with_offset(self, id, offset):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "/products" + "?offset=" + str(offset), verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def add_products(self, id, product_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/products", data=product_object, verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def update_products(self, id, product_id, product_object):
        return requests.put(self.config.base_url + self.path + "/" + str(id) + "/products/" + str(product_id), data=product_object, verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete_product(self, id, product_id):
        return requests.delete(self.config.base_url + self.path + "/" + str(id) + "/products/" + str(product_id), verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete(self, id):
        raise NotImplementedError("Not possible to delete a product")
