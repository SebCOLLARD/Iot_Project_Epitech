#!/usr/bin/env python3

import requests
from requests.structures import CaseInsensitiveDict


class HttpProtocol:
    """
    HTTP Protocol for interactions with Thingsboard.
    """

    def post(url: str, dataJSON: str) -> str:
        """
        POST request over HTTP.

        Params:
        - url (str): The full URL to which the request will be made
        - dataJSON (str): JSON for the request body

        Returns the text of the response.
        """
        header = CaseInsensitiveDict()
        header["Content-Type"] = "application/json"
        respons = requests.post(url, headers=header, data=dataJSON)
        if respons.status_code != requests.codes.ok:
            print("HTTP Error: Code ", respons.status_code)
        else:
            return respons.text
