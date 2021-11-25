#!/usr/bin/env python3

import requests
from requests.structures import CaseInsensitiveDict

class http_protocol:
    def post(url : str, dataJSON: str) -> str:
        respons = requests.post(url, dataJSON)
        header = CaseInsensitiveDict()
        header["Content-Type"] = "application/json"
        respons = requests.post(url, headers = header, data = dataJSON)
        if respons.status_code != requests.codes.ok:
            print('HTTP Error: Code ', respons.status_code)
        else:
            return respons.text
