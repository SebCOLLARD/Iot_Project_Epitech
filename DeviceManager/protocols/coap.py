from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message
from coapthon import defines

from ..config import THINGSBOARD_URL, COAP_PORT


class CoapClient:
    _ct = {"content_type": defines.Content_types["application/json"]}

    def __init__(self, base_url: str = THINGSBOARD_URL) -> None:
        self._client: HelperClient = HelperClient(server=(base_url, COAP_PORT))
        # self.base_url = base_url

    def __del__(self):
        self._client.close()

    def get(self, route, callback=None, timeout=None) -> Message:
        return self._client.get(route, callback=callback, timeout=timeout)
        # self._client.stop()
        # return res

    def put(self, route, payload, callback=None, timeout=None) -> Message:
        return self._client.put(
            route, payload, callback=callback, timeout=timeout, **self._ct
        )

    def post(self, route, payload, callback=None, timeout=None) -> Message:
        return self._client.post(
            route, payload, callback=callback, timeout=timeout, **self._ct
        )

    def delete(self, route, payload, callback=None, timeout=None) -> Message:
        return self._client.delete(
            route, payload, callback=callback, timeout=timeout, **self._ct
        )
