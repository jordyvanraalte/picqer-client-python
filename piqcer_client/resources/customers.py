import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Customers(Resource):
    def __init__(self):
        super().__init__("customers")

    def get_customer_addresses(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "addresses", verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def post_customer_address(self, id, addresses):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "addresses", data=addresses,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def put_customer_address(self, id, address_id, address):
        return requests.put(self.config.base_url + self.path + "/" + str(id) + "addresses/" + str(address_id),
                            data=address,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete_customer_address(self, id, address_id):
        return requests.delete(self.config.base_url + self.path + "/" + str(id) + "/addresses/" + address_id,
                               verify=True,
                               auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete(self, id):
        raise NotImplementedError("Not possible to delete a product")
