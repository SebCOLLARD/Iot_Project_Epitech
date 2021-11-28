#!/usr/bin/env python3

from DeviceManager.config import *
from DeviceManager.protocols.http_protocol import http_protocol
import random
import json


class TemperatureSensor:

    _valueRand : dict = {
        'validTemp' : [-10, 35],
        'invalidTempNeg' : [-100, -10],
        'invalidTempPos' : [36, 100]
    }

    def __init__(self) -> None:
        self._temperature : float = 0.0
        self._humidity : int = 0
        self.generateData()

    def getTemperature(self) -> float:
        return self._temperature

    def getHumdity(self) -> int:
        return self._humidity

    def getValidData(self):
        return round(random.uniform(self._valueRand['validTemp'][0], self._valueRand['validTemp'][1]), 2)

    def getInvalidData(self):
        negatifTemp = round(random.uniform(self._valueRand['invalidTempNeg'][0], self._valueRand['invalidTempNeg'][1]), 2)
        positifTemp = round(random.uniform(self._valueRand['invalidTempPos'][0], self._valueRand['invalidTempPos'][1]), 2)
        return random.choices([negatifTemp, positifTemp], [10, 10], k=1)[0]

    def getValidityTemp(self, temp : float) -> bool:
        if temp >= self._valueRand['validTemp'][0] and temp <= self._valueRand['validTemp'][1]:
            return True
        else:
            return False

    def getTelemetryData(self) -> str:
        data : dict = {
            'temperature': self.getTemperature(),
            'humidity': self.getHumdity(),
            'validityData': self.getValidityTemp(self.getTemperature())
        }
        return json.dumps(data)

    def _setTemperature(self, temp: float) -> None:
        self._temperature = temp

    def _setHumidity(self, humidity: int) -> None:
        self._humidity = humidity

    def generateData(self) -> None:
        validData = self.getValidData()
        invalidData = self.getInvalidData()
        self._setTemperature(random.choices([validData, invalidData], [18, 2], k=1)[0])
        self._setHumidity(random.randrange(0, 101))

    def sendTelemetry(self, token : str) -> None:
        url : str = THINGSBOARD_TELEMETRY_URL
        url = 'http://' + url
        url = url.replace('$ACCES_TOKEN', token)
        data : str = self.getTelemetryData()
        respons : json = http_protocol.post(url, data)
        print(respons)

    def send(self, token : str) -> None:
        self.sendTelemetry(token)
