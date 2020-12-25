import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Orders(Resource):
    def __init__(self):
        super().__init__("orders")

    def process_order(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + '/process', verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def reopen_order(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/reopen", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def force_cancel(self, id):
        return requests.delete(self.config.base_url + self.path + "/" + str(id) + "?force=true", verify=True,
                               auth=HTTPBasicAuth(self.config.api_key, ''))

    def undo_cancellation(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/undo_cancellation", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def product_status(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "/productstatus", verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_notes(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "/notes", verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def post_notes(self, id, notes_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/notes", data=notes_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_tags(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + "/tags", verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def add_tag(self, id, tag_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/tags", data=tag_object, verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete_tag(self, id, tag_id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/tags/" + str(tag_id), verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def allocate_order(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/allocate", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def deallocate_order(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/deallocate", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def prioritise_order(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/prioritise", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def add_product(self, id, product_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/products", data=product_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def update_product(self, id, idorder_product, product_object):
        return requests.put(self.config.base_url + self.path + "/" + str(id) + "/products/" + str(idorder_product),
                            data=product_object,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def remove_product(self, id, idorder_product):
        return requests.delete(self.config.base_url + self.path + "/" + str(id) + "/products/" + str(idorder_product),
                               verify=True,
                               auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_backorder(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + '/backorders', verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))
