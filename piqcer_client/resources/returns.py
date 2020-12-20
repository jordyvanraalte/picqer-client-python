import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Returns(Resource):
    def __init__(self):
        super().__init__("returns")


    def get_returned_products(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "/returned_products",
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def add_returned_product(self, id, returned_product_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/returned_products", data=returned_product_object, verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def update_product(self, id, idreturn_product, returned_product_object):
        return requests.put(self.config.base_url + self.path + "/" + str(id) + "/returned_products/" + str(idreturn_product), data=returned_product_object, verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def delete_product(self, id, idreturn_product):
        return requests.delete(self.config.base_url + self.path + "/" + str(id) + "/returned_products/" + str(idreturn_product), verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def get_replacement_product(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "/replacement_products",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def add_replacement_product(self, id, replacement_product_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/replacement_products",
                             data=replacement_product_object, verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def update_replacement_product(self, id, idreturn_product_replacement, replacement_product_object):
        return requests.put(
            self.config.base_url + self.path + "/" + str(id) + "/replacement_products/" + str(idreturn_product_replacement),
            data=replacement_product_object, verify=True,
            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def delete_replacement_product(self, id, idreturn_product_replacement):
        return requests.delete(
            self.config.base_url + self.path + "/" + str(id) + "/replacement_products/" + str(idreturn_product_replacement),
            verify=True,
            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def get_logs(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "/logs",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def add_comment(self, id, comment_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/logs", data=comment_object,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def receive(self, id, receive_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/receive",
                             data=receive_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()
    def delete(self, id):
        return requests.delete(self.config.base_url + self.path + "/" + str(id), verify=True,
                               auth=HTTPBasicAuth(self.config.api_key, '')).json()
