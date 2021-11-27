import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler

from ..gui.main_window import MainWindow, QApplication, QIcon
from ..devices import FlowSensor, InkSensor, SubstanceSensor
from ..config import INK_SENSOR_TOKEN, FLOW_SENSOR_TOKEN, SUBSTANCE_SENSOR_TOKEN
from ..light_mqtt import LightMqtt


def run_gui(args: list = None):
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    if args is None:
        args = []
    app = QApplication(args)
    app.setWindowIcon(QIcon(os.path.join(os.getcwd(), "icon.ico")))
    sched = BackgroundScheduler()
    FlowSensor(sched, FLOW_SENSOR_TOKEN)
    InkSensor(sched, INK_SENSOR_TOKEN)
    SubstanceSensor(sched, SUBSTANCE_SENSOR_TOKEN)
    LightMqtt(
        "v1/devices/me/attributes",
        "v1/devices/me/rpc/request/+",
        "XBe10xeaw8fpF6bqRr7M",
    )
    LightMqtt(
        "v1/devices/me/attributes",
        "v1/devices/me/rpc/request/+",
        "ZsaUJIHhsCDmobiHcc3u",
    )
    LightMqtt(
        "v1/devices/me/attributes",
        "v1/devices/me/rpc/request/+",
        "8aTocC8taPVNsYRKLjWz",
    )
    MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sched.start()
    sys.exit(app.exec())


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    print(sys.argv, type(sys.argv))
    run_gui(sys.argv)
