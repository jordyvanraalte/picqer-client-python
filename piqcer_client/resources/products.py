import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Products(Resource):
    def __init__(self):
        super().__init__("products")

    def activate_product(self, id):
        return requests.post(self.config.base_url + self.path + '/' + str(id),
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_warehouse_settings(self, id):
        return requests.get(self.config.base_url + self.path + '/' + str(id) + "/warehouses",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def update_warehouse_settings(self, product_id, warehouse_id, settings_object):
        return requests.put(self.config.base_url + self.path + "/" + str(product_id) + "/warehouses/" + str(settings_object), data=object, verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_images(self, id):
        return requests.get(self.config.base_url + self.path + '/' + str(id) + "/images",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def post_images(self, id, image_object):
        return requests.post(self.config.base_url + self.path + '/' + str(id) + "/images", data=image_object,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete_image(self, id, image_id):
        return requests.delete(self.config.base_url + self.path + '/' + str(id) + "/images/" + str(image_id),
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_locations(self, id):
        return requests.get(self.config.base_url + self.path + '/' + str(id) + "/locations",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def link_product(self, id, link_product_object):
        return requests.post(self.config.base_url + self.path + '/' + str(id) + "/locations",
                            data=link_product_object,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def unlink_product(self, id, location_id):
        return requests.post(self.config.base_url + self.path + '/' + str(id) + "/locations/" + location_id,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_tag(self, id):
        return requests.get(self.config.base_url + self.path + '/' + str(id) + "/tags",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def post_tag(self, id, tag_object):
        return requests.post(self.config.base_url + self.path + '/' + str(id) + "/tags",
                             data=tag_object,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def remove_tag(self, id, tags_id):
        return requests.delete(self.config.base_url + self.path + '/' + str(id) + "/tags/" + tags_id,
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_stock(self, id):
        return requests.get(self.config.base_url + self.path + '/' + str(id) + "/stock",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def get_stock_in_single_warehouse(self, product_id, warehouse_id):
        return requests.get(self.config.base_url + self.path + '/' + str(product_id) + "/stock/" + str(warehouse_id),
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def change_stock(self, product_id, warehouse_id, stock_object):
        return requests.post(self.config.base_url + self.path + '/' + str(product_id) + "/stock/" + str(warehouse_id),
                             data=stock_object,
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, ''))

    def move_stock(self, product_id, warehouse_id, stock_object):
        return requests.post(
            self.config.base_url + self.path + '/' + str(product_id) + "/stock/" + str(warehouse_id) + "/move",
            data=stock_object,
            verify=True,
            auth=HTTPBasicAuth(self.config.api_key, ''))

    def delete(self, id):
        raise NotImplementedError("Not possible to delete a product")

