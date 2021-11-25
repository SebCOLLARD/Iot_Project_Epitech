from sys import exit

from apscheduler.schedulers.background import BackgroundScheduler

from DeviceManager.protocols.coap import CoapThingsboardClient
from DeviceManager.devices.fluid_sensor import *


# def cb(*args):
#     print(*args)


# c = CoapClient()
# res = c.get("/", callback=cb)
# print(res)
# print("end")

sched = BackgroundScheduler()

flow = FlowSensor(sched, seconds=5)
# ink = InkSensor(sched)
# substance = SubstanceSensor(sched)

sched.start()
while True:
    continue
