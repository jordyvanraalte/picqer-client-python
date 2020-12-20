import requests
from requests.auth import HTTPBasicAuth
from ..config.config import Config


class Resource:
    def __init__(self, path):
        self.path = path
        self.config = Config()

    def get_all(self):
        return requests.get(self.config.base_url + self.path, verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def get_all_with_offset(self, offset):
        return requests.get(self.config.base_url + self.path + "?offset=" + str(offset), verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def get_with_filter(self, filters):
        return requests.get(self.config.base_url + self.path + str(filters), verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def get(self, id):
        return requests.get(self.config.base_url + self.path + "/" + str(id), verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def post(self, object):
        return requests.post(self.config.base_url + self.path, data=object, verify=True,
                             auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def put(self, id, object):
        return requests.put(self.config.base_url + self.path + "/" + str(id), data=object, verify=True,
                            auth=HTTPBasicAuth(self.config.api_key, '')).json()

    def delete(self, id):
        return requests.delete(self.config.base_url + self.path + "/" + str(id), verify=True,
                               auth=HTTPBasicAuth(self.config.api_key, '')).json()
