import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Backorders(Resource):
    def __init__(self):
        super().__init__("backorders")

    def post(self, object):
        raise NotImplementedError("Not possible to post a backorder")

    def put(self, object):
        raise NotImplementedError("Not possible to put a backorder")

    def process(self):
        return requests.post(self.config.base_url + self.path +  "/process",
                             verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()
