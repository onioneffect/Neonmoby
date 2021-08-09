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

def neon_api_caller(*args, **kwargs):
    pass

def get_set_by_id(id_num : int) -> Set:
    return Set(r.get(neonmob.SET_URL.format(id_num)))

def get_user_by_id(user_id_num : int) -> Set:
    return Set(r.get(neonmob.USER_URL.format(user_id_num)))
    # TODO: Make a parent class with the current __init__ method.
    # TODO: Make a function to easily call all of these endpoints.
