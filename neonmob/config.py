class Settings:
    http_lib = __import__("requests")
    getter = http_lib.get
    