import json
import requests


class Web:
    """docstring for SpiderWeb."""

    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint
        # print(f"[WEB] endpoint: {self.api_endpoint}")


    def POST(self, data):
        # loading a json dump helps avoid NoneType errorr
        #   when decoding within Flask
        jdata = json.loads(json.dumps(data))
        r = requests.post(self.api_endpoint, json=jdata)
        return r.status_code


    def get_assignment(self):
        pass


    def feed_list(self, lst):
        pass


    def report_back(self, egg):
        pass




#
