#!/usr/bin/env python3

import paho.mqtt.client as mqtt

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerAlreadyRunningError
from .devices import LightSensor
import threading
import json


class LightMqtt:
    _ip = "thingsboard.matthieu-rochette.fr"
    _port = 1883
    _socketTimes = 1

    def __init__(self, topicSend, topicRecived, access_token):
        self.topicSend = topicSend
        self.topicRecived = topicRecived
        self.accessToken = access_token
        self.scheduler: BackgroundScheduler = BackgroundScheduler()
        self.light = LightSensor()
        self.client = mqtt.Client()
        self.client.username_pw_set(username=self.accessToken)
        self.thread = threading.Thread(target=self.start)
        self.thread.start()

    def __del__(self):
        print("\n\n\n\nIN DEL\n\n\n\n")
        self.stopThread()

    def send(self):
        self.client.publish(self.topicSend, str(self.light.get_all()), 0)
        self.client.publish("v1/devices/me/telemetry", str(self.light.get_all()), 0)

    def receiver(self):
        def wrapper(client, user_data, msg):
            val = str(msg.payload).split("'")[1]
            if val is None:
                return
            jsonData = json.loads(val)
            if jsonData is None:
                return
            try:
                params = jsonData["params"]
                method = jsonData["method"]
            except KeyError:
                return
            else:
                if params is None or method is None:
                    return
                if method == self.accessToken + "_switch" and params == True:
                    self.light.light_on()
                elif method == self.accessToken + "_switch" and params == False:
                    self.light.light_off()
                if method == self.accessToken + "_intensity":
                    self.light.set_intensity(params)
                if method == self.accessToken + "_color":
                    self.light.set_color_temp(params)

        return wrapper

    def start(self):
        self.client.connect(LightMqtt._ip, LightMqtt._port, 60)
        self.client.subscribe(self.topicRecived)
        self.client.on_message = self.receiver()
        self.job = self.scheduler.add_job(
            self.send, "interval", seconds=LightMqtt._socketTimes
        )
        try:
            self.scheduler.start()
        except SchedulerAlreadyRunningError:
            pass
        self.client.loop_forever()

    def stopThread(self):
        self.scheduler.remove_job(self.job.id)
        self.client.disconnect()
        self.thread.join()
