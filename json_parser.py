import json


def toJson(somelist):
    return json.dumps(somelist, indent=4, ensure_ascii=False)
