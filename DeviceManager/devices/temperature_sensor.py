#!/usr/bin/env python3

import json
import random

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from DeviceManager.config import *
from DeviceManager.protocols.http_protocol import HttpProtocol


class TemperatureSensor:
    """
    Represents a temperature sensor.
    """

    _valueRand: dict = {
        "validTemp": [-10, 35],
        "invalidTempNeg": [-100, -10],
        "invalidTempPos": [36, 100],
    }

    def __init__(self, token: str, scheduler: BackgroundScheduler) -> None:
        self._token: str = token
        self._scheduler = scheduler
        self._job = self._scheduler.add_job(
            self.send, trigger=IntervalTrigger(seconds=1)
        )
        self._temperature: float = 0.0
        self._humidity: int = 0
        self.generateData()

    def send(self) -> None:
        """
        Generate new data and send it to Thingsboard.
        """
        self.generateData()
        self.sendTelemetry()

    def getJob(self) -> None:
        """
        Get the job currently in the scheduler.
        """
        return self._job

    def getTemperature(self) -> float:
        """
        Get the current temperature.
        """
        return self._temperature

    def getHumdity(self) -> int:
        """
        Get the current humidity.
        """
        return self._humidity

    def getValidData(self):
        """
        Get a random valid temperature data.
        """
        return round(
            random.uniform(
                self._valueRand["validTemp"][0], self._valueRand["validTemp"][1]
            ),
            2,
        )

    def getInvalidData(self):
        """
        Get a random invalid temperature data.
        """
        negatifTemp = round(
            random.uniform(
                self._valueRand["invalidTempNeg"][0],
                self._valueRand["invalidTempNeg"][1],
            ),
            2,
        )
        positifTemp = round(
            random.uniform(
                self._valueRand["invalidTempPos"][0],
                self._valueRand["invalidTempPos"][1],
            ),
            2,
        )
        return random.choices([negatifTemp, positifTemp], [10, 10], k=1)[0]

    def getValidityTemp(self, temp: float) -> bool:
        """
        Verify if a given temperature is considered valid.

        Params:
        - temp (float): The temperature to verify.

        Returns `True` if the temperature is valid, `False` otherwise.
        """
        if (
            temp >= self._valueRand["validTemp"][0]
            and temp <= self._valueRand["validTemp"][1]
        ):
            return True
        else:
            return False

    def getTelemetryData(self) -> str:
        """
        Returns a JSON payload to send to Thingsboard's telemetry feature.
        """
        data: dict = {
            "temperature": self.getTemperature(),
            "humidity": self.getHumdity(),
            "validityData": self.getValidityTemp(self.getTemperature()),
        }
        return json.dumps(data)

    def _setTemperature(self, temp: float) -> None:
        """
        Set the current temperature.

        Params:
        - temp (float): the new temperature.
        """
        self._temperature = temp

    def _setHumidity(self, humidity: int) -> None:
        """
        Set the current humidity.

        Params:
        - humidity (float): the new humidity.
        """
        self._humidity = humidity

    def generateData(self) -> None:
        """
        Generate new temperature and humidity.
        """
        validData = self.getValidData()
        invalidData = self.getInvalidData()
        self._setTemperature(random.choices([validData, invalidData], [18, 2], k=1)[0])
        self._setHumidity(random.randrange(0, 101))

    def sendTelemetry(self) -> None:
        """
        Send data to Thingsboard.

        Params:
        - token (str): The Thingsboard device's access token.
        """
        url: str = THINGSBOARD_TELEMETRY_URL
        url = "http://" + url
        url = url.replace("$ACCES_TOKEN", self._token)
        data: str = self.getTelemetryData()
        HttpProtocol.post(url, data)
