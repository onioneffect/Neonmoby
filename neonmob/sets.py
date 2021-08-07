import requests as r
import json

ROOT_URL = "https://neonmob.com/api/"

class Set:
    def __init__(self, resp : r.models.Response):
        json_dict = json.loads(resp.text)

        for key in json_dict.keys():
            setattr(self, key, json_dict[key])

    def get_values(self, *args) -> tuple:
        return_list = []

        for key in args:
            try:
                return_list.append(getattr(self, key))
            except AttributeError:
                pass

        return tuple(return_list)

def get_set_by_id(id_num : int) -> Set:
    return Set(r.get(ROOT_URL + f"setts/{id_num}/"))
