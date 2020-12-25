from ..resources.resource import Resource


class VatGroup(Resource):
    def __init__(self):
        super().__init__("vatgroups")

    def post(self, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def put(self, id, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def delete(self, id):
        raise NotImplementedError("Not possible to post a warehouse")