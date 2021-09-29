class Settings:
    http_lib = __import__("requests")
    getter = http_lib.get
    resp_class = http_lib.models.Response

class URLLIB_SETTINGS:
    http_lib = __import__("urllib")
    getter = http_lib.request.urlopen

    ref = __import__("http")
    resp_class = ref.client.HTTPResponse
