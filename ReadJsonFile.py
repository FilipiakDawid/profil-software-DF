import json


def readfile(file):
    with open(file, encoding="utf8") as f:
        d = json.load(f)
    return d