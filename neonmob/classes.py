import neonmob
import json

class NeonResponse:
    def __init__(self, resp):
        if isinstance(resp, neonmob.Settings.resp_class):
            print("Working isinstance!")
        else:
            print("isinstance returns false!")

        content = resp.text
        json_dict = json.loads(content)

        for key in json_dict.keys():
            setattr(self, key, json_dict[key])

    def get_values(self, *args) -> tuple:
        return tuple(getattr(self, key) for key in args)

class Set(NeonResponse):
    pass

class User(NeonResponse):
    pass
