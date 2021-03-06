from ..resources.resource import Resource
import requests
from requests.auth import HTTPBasicAuth


class OrderFields(Resource):
    def __init__(self):
        super().__init__("orderfields")

    def post(self, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def put(self, id, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def delete(self, id):
        raise NotImplementedError("Not possible to post a warehouse")