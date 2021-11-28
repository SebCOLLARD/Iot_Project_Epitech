#!/usr/bin/env python3

from .devices.temperature_sensor import TemperatureSensor
from apscheduler.schedulers.background import BackgroundScheduler


class temperature_sensor:
    def __init__(self, token: str, scheduler: BackgroundScheduler) -> None:
        self._token: str = token
        self._tempSensor: TemperatureSensor = TemperatureSensor()
        self._scheduler = scheduler
        self._job = self._scheduler.add_job(self.send, "interval", seconds=2)

    def send(self):
        self._tempSensor.generateData()
        jsonData: str = self._tempSensor.rawToJSON()
        self._tempSensor.sendData(jsonData, self._token)

    def getJob(self):
        return self._job
