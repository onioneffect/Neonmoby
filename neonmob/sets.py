# TODO: Make a parent class with the current __init__ method.

import neonmob
import requests as r
import json

class Set:
    def __init__(self, resp : r.models.Response):
        self.response = resp
        json_dict = json.loads(resp.text)

        for key in json_dict.keys():
            setattr(self, key, json_dict[key])

    def get_values(self, *args) -> tuple:
        return tuple(getattr(self, key) for key in args)
