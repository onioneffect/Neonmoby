import neonmob
import requests as r

def neon_api_caller(**kwargs):
    return neonmob.Set(r.get(kwargs["endpoint"].format(kwargs["fmt"])))

def get_set_by_id(id_num : int) -> neonmob.Set:
    return neon_api_caller(endpoint=neonmob.urls.SET_URL, fmt=id_num)

def get_user_by_id(user_id_num : int) -> neonmob.Set:
    return neon_api_caller(endpoint=neonmob.urls.USER_URL, fmt=user_id_num)
