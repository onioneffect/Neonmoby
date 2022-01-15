import requests as r
import json

from neonmob.urls import ROOT_URL

class NeonResponse:
    def __init__(self, resp : r.models.Response):
        self.response = resp
        json_dict = json.loads(resp.text)

        for key in json_dict.keys():
            setattr(self, key, json_dict[key])

    # In case your set can't be found, it will probably
    # raise an AttributeError, because it has no "id" key
    def get_values(self, *args) -> tuple:
        return tuple(getattr(self, key) for key in args)

class Set(NeonResponse):
    pass

class Tiers(NeonResponse):
    pass

class User(NeonResponse):
    pass
