from coapthon import defines
from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message

from ..config import COAP_PORT, THINGSBOARD_URL


class CoapThingsboardClient:
    """
    A CoAP client for to interact with Thingsboard
    """

    _ct = {"content_type": defines.Content_types["application/json"]}
    route_post = "/api/v1/{access_token}/telemetry"

    def __init__(self, base_url: str = THINGSBOARD_URL) -> None:
        """
        Params:
        - base_url (str): The URL of the Thingsboard server
        """
        self._client: HelperClient = HelperClient(server=(base_url, COAP_PORT))

    def __del__(self):
        self._client.close()

    def get(self, route, callback=None, timeout=None) -> Message:
        """
        GET request over CoAP.

        Params:
        - route (str): the route to append to the server's URL
        - callback (callable): a function to call upon reception of the response
        - timeout(int): amount of time before abandoning request if waiting for response

        Returns a `Message` instance containing the response.
        """
        return self._client.get(route, callback=callback, timeout=timeout)

    def put(self, route, payload, callback=None, timeout=None) -> Message:
        """
        PUT request over CoAP.

        Params:
        - route (str): the route to append to the server's URL
        - payload (str): body of the request
        - callback (callable): a function to call upon reception of the response
        - timeout(int): amount of time before abandoning request if waiting for response

        Returns a `Message` instance containing the response.
        """
        return self._client.put(
            route, payload, callback=callback, timeout=timeout, **self._ct
        )

    def post(self, access_token, payload, callback=None, timeout=None) -> Message:
        """
        POST request over CoAP.

        Params:
        - route (str): the route to append to the server's URL
        - payload (str): body of the request
        - callback (callable): a function to call upon reception of the response
        - timeout(int): amount of time before abandoning request if waiting for response

        Returns a `Message` instance containing the response.
        """
        return self._client.post(
            self.route_post.format(access_token=access_token),
            payload,
            callback=callback,
            timeout=timeout,
            **self._ct
        )

    def delete(self, route, payload, callback=None, timeout=None) -> Message:
        """
        DELETE request over CoAP.

        Params:
        - route (str): the route to append to the server's URL
        - payload (str): body of the request
        - callback (callable): a function to call upon reception of the response
        - timeout(int): amount of time before abandoning request if waiting for response

        Returns a `Message` instance containing the response.
        """
        return self._client.delete(
            route, payload, callback=callback, timeout=timeout, **self._ct
        )
