""" Python script that fetches https://alu-intranet.hbtn.io/status using requests package.
"""

import requests
from requests import Request

url = "https://alu-intranet.hbtn.io/status"

req = Request("GET", url)

if __name__ == "__main__":
    r = requests.get(url)
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)