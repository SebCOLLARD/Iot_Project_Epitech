import logging
from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Thingsboard URLs
THINGSBOARD_URL = getenv("THINGSBOARD_URL", "thingsboard.matthieu-rochette.fr")
THINGSBOARD_TELEMETRY_URL: str = f"{THINGSBOARD_URL}/api/v1/$ACCES_TOKEN/telemetry"
THINGSBOARD_ATTRIBUTES_URL: str = f"{THINGSBOARD_URL}/api/v1/$ACCES_TOKEN/attributes"
LIGHT_DASHBOARD_URL = getenv(
    "LIGHT_DASHBOARD_URL",
    "http://thingsboard.matthieu-rochette.fr/dashboard/6fcca880-4eea-11ec-96b5-35454323bc15?publicId=e942da30-4dd8-11ec-a7fc-35454323bc15",
)
TEMPERATURE_DASHBOARD_URL = getenv(
    "TEMPERATURE_DASHBOARD_URL",
    "http://thingsboard.matthieu-rochette.fr/dashboard/b5102520-4ea4-11ec-96b5-35454323bc15?publicId=e942da30-4dd8-11ec-a7fc-35454323bc15",
)

# CoAP PORT to use on Thingsboard instance
COAP_PORT = int(getenv("COAP_PORT", 5683))

# Thingsboard devices' access tokens
INK_SENSOR_TOKEN = getenv("INK_SENSOR_TOKEN", "QmA8R32flxPfMNS5Sc5v")
FLOW_SENSOR_TOKEN = getenv("FLOW_SENSOR_TOKEN", "RO28FyiHnz1lIciKuK20")
SUBSTANCE_SENSOR_TOKEN = getenv("SUBSTANCE_SENSOR_TOKEN", "GTZnZzYfX2CSMr7uFmhF")
TEMP_1_TOKEN = getenv("TEMP_1_TOKEN", "z1rVnmZC7JengspAeFdb")
TEMP_2_TOKEN = getenv("TEMP_2_TOKEN", "1tU9nolQfpMccVRRbHhW")
TEMP_3_TOKEN = getenv("TEMP_3_TOKEN", "AOfzo5udNbq3dg1XOvUi")
LIGHT_1_TOKEN = getenv("LIGHT_1_TOKEN", "XBe10xeaw8fpF6bqRr7M")
LIGHT_2_TOKEN = getenv("LIGHT_2_TOKEN", "ZsaUJIHhsCDmobiHcc3u")
LIGHT_3_TOKEN = getenv("LIGHT_3_TOKEN", "8aTocC8taPVNsYRKLjWz")

# Log level
LOG_LEVEL = getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL)
