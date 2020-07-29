import json
from app.utilities.helpers import find_nodes


class GraphData:
    def __init__(self, data):
        self.data = self.load_data(data)
        try:
            self.nodes = find_nodes(self.data, "data")
            self.page_info = find_nodes(self.data, "pageInfo")
        except KeyError as error:
            print("An error happened: {}".format(error))

    @staticmethod
    def load_data(data):
        try:
            return json.loads(data)
        except Exception as error:
            print("An error was encountered: {}".format(error))
            return error
