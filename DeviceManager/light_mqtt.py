#!/usr/bin/env python3

import json
import threading

import paho.mqtt.client as mqtt
from apscheduler.schedulers import SchedulerAlreadyRunningError
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from .devices import LightSensor


class LightMqtt:
    """
    Implementation of MQTT protocol to connect the device to the server.
    """

    _ip = "thingsboard.matthieu-rochette.fr"
    _port = 1883
    _socketTimes = 1

    def __init__(self, topicSend, topicRecived, access_token):
        """
        topicSend = MQTT topic where to send data.
        topicReceive = MQTT topic where to receive data.
        access_token = Thingsboard device token.
        scheduler = Initialise the background scheduler.
        light = Initialise light sensor class.
        client = Initialise MQTT client.
        thread = Initialise a thread.
        """
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
        """
        Stop the thread.
        """
        print("\n\n\n\nIN DEL\n\n\n\n")
        self.stopThread()

    def send(self):
        """
        Using MQTT send data on topicSend and telemetry topic.
        """
        self.client.publish(self.topicSend, str(self.light.get_all()), 0)
        self.client.publish("v1/devices/me/telemetry", str(self.light.get_all()), 0)

    def receiver(self):
        """
        Receive data form thingsboard controller.
        """

        def wrapper(client, user_data, msg):
            """
            Call light sensor method to change the state, the intensity and the color temperature.
            """
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
        """
        Connect the client to the server and send the data.
        """
        self.client.connect(LightMqtt._ip, LightMqtt._port, 60)
        self.client.subscribe(self.topicRecived)
        self.client.on_message = self.receiver()
        self.job = self.scheduler.add_job(
            self.send, trigger=IntervalTrigger(seconds=LightMqtt._socketTimes)
        )
        try:
            self.scheduler.start()
        except SchedulerAlreadyRunningError:
            pass
        self.client.loop_forever()

    def stopThread(self):
        """
        Stop all background processes.
        """
        self.scheduler.remove_all_jobs()
        self.client.disconnect()
        self.thread.join()
