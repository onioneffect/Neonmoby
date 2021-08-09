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
        return_list = []

        for key in args:
            try:
                return_list.append(getattr(self, key))
            except AttributeError:
                pass

        return tuple(return_list)

def get_set_by_id(id_num : int) -> Set:
    return Set(r.get(neonmob.SET_URL.format(id_num)))

def get_user_by_id(user_id_num : int) -> Set:
    return Set(r.get(neonmob.USER_URL.format(user_id_num)))
    # TODO: Make a parent class with the current __init__ method.
    # TODO: Make a function to easily call all of these endpoints.
