from os import getenv

from dotenv import load_dotenv

load_dotenv()

THINGSBOARD_URL = getenv("THINGSBOARD_URL", "thingsboard.matthieu-rochette.fr")
COAP_PORT = int(getenv("COAP_PORT", 5683))

OVERPASS_API_URL : str = getenv('OVERPASS_API_URL', 'http://overpass-api.de/api/interpreter')
OVERPASS_QUERY : str = getenv('OVERPASS_QUERY', '[out:json];area[name="Paris"];(node[amenity="cafe"](area););out;')
THINGSBOARD_PROTOCOL_URL : str = f'{THINGSBOARD_URL}/api/v1/$ACCES_TOKEN/telemetry'
