#!/usr/bin/env python3

import requests
import json

class http_protocol:
    def post(url : str, dataJSON: json):
        response = requests.post(url, dataJSON)
        if response.status_code != requests.codes.ok:
            print('HTTP Error: Code ', response.status_code)
