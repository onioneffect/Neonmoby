import neonmob
import requests as r

def neon_api_caller(**kwargs):
    if not isinstance(kwargs["class_ref"], type):
        raise TypeError("class_ref must be a class")

    if kwargs["headers"]:
        return_request = r.get(
            kwargs["endpoint"].format(kwargs["fmt"]),
            headers=kwargs["headers"]
        )
    else:
        return_request = r.get(
            kwargs["endpoint"].format(kwargs["fmt"])
        )

    if kwargs["print"]:
        print(return_request.text)

    return_type = kwargs["class_ref"]
    return return_type(return_request)

def get_set_by_id(id_num : int) -> neonmob.Set:
    return neon_api_caller(
        endpoint=neonmob.urls.SET_URL,
        fmt=id_num,
        class_ref=neonmob.Set
    )

def get_pack_tiers_by_id(id_num : int, heads : dict) -> neonmob.Tiers:
    return neon_api_caller(
        endpoint=neonmob.urls.PACKS_URL,
        fmt=id_num,
        class_ref=neonmob.Tiers,
        headers=heads,
        print=True
    )

def get_user_by_id(user_id_num : int) -> neonmob.User:
    return neon_api_caller(
        endpoint=neonmob.urls.USER_URL,
        fmt=user_id_num,
        class_ref=neonmob.User
    )
