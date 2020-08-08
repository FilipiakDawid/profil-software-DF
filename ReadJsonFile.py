import json
import requests


def read_file_local(file):
    try:
        with open(file, encoding="utf8") as f:
            d = json.load(f)
        return d
    except BaseException as err:
        print("Something goes wrong: " + str(err))
        return None


def read_file_from_api(url):
    response = requests.request("GET", url)
    if response.status_code != 200:
        print("Something goes wrong, please try again response code(" + str(response.status_code) + ")")
        return None
    else:
        return response.json()
