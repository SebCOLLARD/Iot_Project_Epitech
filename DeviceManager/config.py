from os import getenv
import logging

from dotenv import load_dotenv

load_dotenv()

THINGSBOARD_URL = getenv("THINGSBOARD_URL", "thingsboard.matthieu-rochette.fr")
COAP_PORT = int(getenv("COAP_PORT", 5683))
LOG_LEVEL = getenv("LOG_LEVEL", "INFO")

INK_SENSOR_TOKEN = getenv("INK_SENSOR_TOKEN", "QmA8R32flxPfMNS5Sc5v")
FLOW_SENSOR_TOKEN = getenv("FLOW_SENSOR_TOKEN", "RO28FyiHnz1lIciKuK20")
SUBSTANCE_SENSOR_TOKEN = getenv("SUBSTANCE_SENSOR_TOKEN", "GTZnZzYfX2CSMr7uFmhF")

logging.basicConfig(level=LOG_LEVEL)
