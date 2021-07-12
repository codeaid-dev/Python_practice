import json

with open("test.json") as fh:
    js = json.loads(fh.read())
    print(js["hello"])
