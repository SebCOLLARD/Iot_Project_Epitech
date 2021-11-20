#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from apscheduler.schedulers.background import BackgroundScheduler
from light import Light

scheduler = BackgroundScheduler()
light = Light()
client = mqtt.Client()

def send():
    client.publish("test/status", str(light.getAll()), 0)

try:
    v = client.connect("127.0.0.1", 1883, 60)
    scheduler.add_job(send, 'interval', seconds=2)
    scheduler.start()
    while 1:
        a=1
except:
    client.disconnect()