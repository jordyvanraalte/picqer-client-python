from ..resources.resource import Resource
import requests
from requests.auth import HTTPBasicAuth


class Suppliers(Resource):
    def __init__(self):
        super().__init__("suppliers")

    def delete(self, id):
        raise NotImplementedError("Not possible to post a warehouse")
