#!/usr/bin/env python3

from DeviceManager.devices.temperature_sensor import TemperatureSensor
from apscheduler.schedulers.background import BackgroundScheduler

class temperature_sensor_main:

    def __init__(self, token : str, scheduler : BackgroundScheduler) -> None:
        self._token : str = token
        self._tempSensor : TemperatureSensor = TemperatureSensor()
        self._scheduler = scheduler
        self._job = self._scheduler.add_job(self.send, "interval", seconds = 2)

    def send(self) -> None:
        self._tempSensor.generateData()
        self._tempSensor.send(self._token)

    def getJob(self) -> None:
        return self._job

scheduler : BackgroundScheduler = BackgroundScheduler()

Sensor_1 = temperature_sensor_main('z1rVnmZC7JengspAeFdb', scheduler)
Sensor_2 = temperature_sensor_main('1tU9nolQfpMccVRRbHhW', scheduler)
Sensor_3 = temperature_sensor_main('AOfzo5udNbq3dg1XOvUi', scheduler)

scheduler.start()
while 42:
    pass
