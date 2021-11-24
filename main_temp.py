#!/usr/bin/env python3

from DeviceManager.devices.temperature_sensor import TemperatureSensor

sensor = TemperatureSensor()
# print('Temperature\t', sensor.getTemperature())
# print('Humidity\t', sensor.getHumdity())
# print('Location\t', sensor.getLocation())
# print('JSON\t', sensor.rawToJSON())

sensor.sendData(sensor.rawToJSON())
# print(sensor.getLocation())
