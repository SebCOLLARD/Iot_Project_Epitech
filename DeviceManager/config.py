from os import getenv
import logging

from dotenv import load_dotenv

load_dotenv()

THINGSBOARD_URL = getenv("THINGSBOARD_URL", "thingsboard.matthieu-rochette.fr")
THINGSBOARD_TELEMETRY_URL : str = f'{THINGSBOARD_URL}/api/v1/$ACCES_TOKEN/telemetry'
THINGSBOARD_ATTRIBUTES_URL : str = f'{THINGSBOARD_URL}/api/v1/$ACCES_TOKEN/attributes'

LIGHT_DASHBOARD_URL = getenv(
    "LIGHT_DASHBOARD_URL",
    "http://thingsboard.matthieu-rochette.fr/dashboard/6fcca880-4eea-11ec-96b5-35454323bc15?publicId=e942da30-4dd8-11ec-a7fc-35454323bc15",
)
TEMPERATURE_DASHBOARD_URL = getenv(
    "TEMPERATURE_DASHBOARD_URL",
    "http://thingsboard.matthieu-rochette.fr/dashboard/b5102520-4ea4-11ec-96b5-35454323bc15?publicId=e942da30-4dd8-11ec-a7fc-35454323bc15",
)
# FLUIDS_DASHBOARD_URL = getenv(
#     "FLUIDS_DASHBOARD_URL",
#     "http://thingsboard.matthieu-rochette.fr/dashboard/a3618da0-4fe4-11ec-96b5-35454323bc15?publicId=e942da30-4dd8-11ec-a7fc-35454323bc15",
# )

COAP_PORT = int(getenv("COAP_PORT", 5683))
LOG_LEVEL = getenv("LOG_LEVEL", "INFO")

INK_SENSOR_TOKEN = getenv("INK_SENSOR_TOKEN", "QmA8R32flxPfMNS5Sc5v")
FLOW_SENSOR_TOKEN = getenv("FLOW_SENSOR_TOKEN", "RO28FyiHnz1lIciKuK20")
SUBSTANCE_SENSOR_TOKEN = getenv("SUBSTANCE_SENSOR_TOKEN", "GTZnZzYfX2CSMr7uFmhF")


logging.basicConfig(level=LOG_LEVEL)
