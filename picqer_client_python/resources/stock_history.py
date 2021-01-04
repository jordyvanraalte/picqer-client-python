from ..resources.resource import Resource


class StockHistory(Resource):
    def __init__(self):
        super().__init__("stockhistory")

    def post(self, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def put(self, id, object):
        raise NotImplementedError("Not possible to post a warehouse")

    def delete(self, id):
        raise NotImplementedError("Not possible to post a warehouse")