import requests
from requests.auth import HTTPBasicAuth
from ..resources.resource import Resource


class Tags(Resource):
    def __init__(self):
        super().__init__("tags")