#!/usr/bin/env python3

from DeviceManager.devices.config_temperature_sensor import *
from DeviceManager.protocols.http_protocol import http_protocol
import random
import json
import requests

class TemperatureSensor:
    def __init__(self) -> None:
        self._temperature : float = 0.0
        self._humidity : int = 0
        self._location : str = ''
        self._setLocation(self.getRandomLocation() + ', ' + random.choice(IntExt))
        self._setAll()

    def getRandomLocation(self) -> str:
        coords : list = []
        res = requests.get(overpassAPI, params={'data': overpassQuery})
        if res.status_code == 200:
            resData = res.json()
            places = resData.get('elements', [])
            for place in places:
                coords.append((place['lat'], place['lon']))
        if len(coords) == 0:
            return '48.8778422, 2.3273653'
        else:
            randomPlace : tuple = random.choice(coords)
            return str(randomPlace[0]) + ', ' + str(randomPlace[1])

    def getTemperature(self) -> float:
        return self._temperature

    def getHumdity(self) -> int:
        return self._humidity

    def getLocation(self) -> str:
        return self._location

    def getValidData(self):
        return round(random.uniform(-50, 100), 2)

    def getInvalidData(sefl):
        negatifTemp = round(random.uniform(-1000, -50.0), 2)
        positifTemp = round(random.uniform(101, 1000), 2)
        return random.choices([negatifTemp, positifTemp], [10, 10], k=1)[0]

    def getValidityTemp(self, temp : float) -> bool:
        if temp >= -50 and temp <= 100.99:
            return True
        else:
            return False

    def _setTemperature(self, temp: float) -> None:
        self._temperature = temp

    def _setHumidity(self, humidity: int) -> None:
        self._humidity = humidity

    def _setLocation(self, loc: str) -> None:
        self._location = loc

    def _setAll(self) -> None:
        validData = self.getValidData()
        invalidData = self.getInvalidData()
        self._setTemperature(random.choices([validData, invalidData], [17, 3], k=1)[0])
        self._setHumidity(random.randrange(0, 101))

    def rawToJSON(self) -> str:
        data : dict = {
            'temperature': self.getTemperature(),
            'humidity': self.getHumdity(),
            'location': self.getLocation(),
            'validityData': self.getValidityTemp(self.getTemperature())
        }
        return json.dumps(data)

    def sendData(self, data : str) -> None:
        http_protocol.post(thinkboardsURL, data)
