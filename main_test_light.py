#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from apscheduler.schedulers.background import BackgroundScheduler
from DeviceManager.devices import LightSensor


class LightMqtt:
    _ip = "127.0.0.1"
    _port = 1883
    _socketTimes = 2

    def __init__(self, topicSend, topicRecived):
        self.topicSend = topicSend
        self.topicRecived = topicRecived
        self.scheduler = BackgroundScheduler()
        self.light = LightSensor()
        self.client = mqtt.Client()

    def send(self):
        self.client.publish(self.topicSend, str(self.light.get_all()), 0)

    def recived(client, userdata, msg):
        val = str(msg.payload).split('\'')[1]
        if val == 'on':
            self.light.light_on()
        elif val == 'off':
            self.light.light_off()
        else:
            print(val)

    def start(self):
        self.client.connect(LightMqtt._ip, LightMqtt._port, 60)
        self.client.subscribe(self.topicRecived)
        self.client.on_message = LightMqtt.recived
        self.scheduler.add_job(self.send, 'interval', seconds=LightMqtt._socketTimes)
        self.scheduler.start()
        self.client.loop_forever()
    
    def stop(self):
        self.client.disconnect()


test = LightMqtt("send", "recived")
test.start()