from ..resources.resource import Resource
import requests
from requests.auth import HTTPBasicAuth


class Users(Resource):
    def __init__(self):
        super().__init__("users")

    def me(self):
        return requests.get(self.config.base_url + self.path + "/me",
                            verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, ''))

    def post(self, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def put(self, id, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def delete(self, id):
        raise NotImplementedError("Not possible to post a warehouse")
