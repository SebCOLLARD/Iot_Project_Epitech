from os import getenv

from dotenv import load_dotenv

load_dotenv()

THINGSBOARD_URL = getenv("THINGSBOARD_URL", "thingsboard.matthieu-rochette.fr")
COAP_PORT = int(getenv("COAP_PORT", 5683))
