import neonmob

fetched = neonmob.get_set_by_id(32)

with open("tests/darwin/darwin.json", "r") as f:
    print(f.read() == fetched.response.text)
