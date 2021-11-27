#!/usr/bin/env python3

from time import sleep
import paho.mqtt.client as mqtt
from apscheduler.schedulers.background import BackgroundScheduler
from DeviceManager.devices import LightSensor
import threading
import json
import pprint


class LightMqtt:
    _ip = "thingsboard.matthieu-rochette.fr"
    _port = 1883
    _socketTimes = 1

    def __init__(self, topicSend, topicRecived, access_token):
        self.topicSend = topicSend
        self.topicRecived = topicRecived
        self.accessToken = access_token
        self.scheduler = BackgroundScheduler()
        self.light = LightSensor()
        self.client = mqtt.Client()
        self.client.username_pw_set(username=self.accessToken)
        self.thread = threading.Thread(target=self.start)
        self.thread.start()

    def send(self):
        self.client.publish(self.topicSend, str(self.light.get_all()), 0)
        self.client.publish("v1/devices/me/telemetry", str(self.light.get_all()), 0)

    def receiver(self):
        def wrapper(client, user_data, msg):

            val = str(msg.payload).split("'")[1]
            jsonData = json.loads(val)
            params = jsonData['params']
            method = jsonData['method']
            if method == self.accessToken and params == True :
                self.light.light_on()
            elif method == self.accessToken and params == False :
                self.light.light_off()
            # self.light.set_intensity(jsonData['intensity'])
            # self.light.set_color_temp(jsonData['color_temp'])

        return wrapper

    def start(self):
        self.client.connect(LightMqtt._ip, LightMqtt._port, 60)
        self.client.subscribe(self.topicRecived)
        self.client.on_message = self.receiver()
        self.scheduler.add_job(self.send, "interval", seconds=LightMqtt._socketTimes)
        self.scheduler.start()
        self.client.loop_forever()
    
    def stopThread(self):
        self.client.disconnect()
        self.thread.join()


test = LightMqtt("v1/devices/me/attributes", "v1/devices/me/rpc/request/+", "XBe10xeaw8fpF6bqRr7M")
test2 = LightMqtt("v1/devices/me/attributes", "v1/devices/me/rpc/request/+", "ZsaUJIHhsCDmobiHcc3u")
test3 = LightMqtt("v1/devices/me/attributes", "v1/devices/me/rpc/request/+", "8aTocC8taPVNsYRKLjWz")

test.stopThread()
test2.stopThread()
test3.stopThread()