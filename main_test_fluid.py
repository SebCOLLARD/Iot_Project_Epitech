from sys import exit

from apscheduler.schedulers.blocking import BlockingScheduler

from DeviceManager.protocols.coap import CoapClient
from DeviceManager.devices.fluid_sensor import *


# def cb(*args):
#     print(*args)


# c = CoapClient()
# res = c.get("/", callback=cb)
# print(res)
# print("end")

sched = BlockingScheduler()

flow = FlowSensor(sched, seconds=5)
# ink = InkSensor(sched)
# substance = SubstanceSensor(sched)

try:
    sched.start()
except KeyboardInterrupt:
    sched.shutdown()
    exit(0)
