import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Warehouses(Resource):
    def __init__(self):
        super().__init__("warehouses")

    def post(self, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def put(self, id, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def delete(self, id):
        raise NotImplementedError("Not possible to post a warehouse")