import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Picklists(Resource):
    def __init__(self):
        super().__init__("picklists")

    def close_picklist(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/close", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def pick_product(self, id, product_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/pick", data=product_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def pick_all(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/pickall", verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_shipments(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + '/shipments', verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_shipping_methods(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id) + '/shippingmethods', verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def create_shipments(self, id, shipments_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + '/shipments', data=shipments_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def assign_user(self, id, user_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/assign", data=user_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def unassign_user(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/unassign",
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_pdf_json(self, id):
        headers = {"Accept": "application/json"}
        return requests.get(self.config.base_url + self.path + "/" + str(id) + '/picklistpdf', verify=True,
                            headers=headers,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_packing_list_pdf_json(self, id):
        headers = {"Accept": "application/json"}
        return requests.get(self.config.base_url + self.path + "/" + str(id) + '/packinglistpdf', verify=True,
                            headers=headers,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def snooze(self, id, snooze_object):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/snooze", data=snooze_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def cancel(self, id):
        return requests.post(self.config.base_url + self.path + "/" + str(id) + "/cancel",
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete(self, id):
        raise NotImplementedError("Not possible to delete a product")