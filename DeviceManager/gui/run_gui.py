import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler

from ..gui.main_window import MainWindow, QApplication, QIcon
from ..devices import FlowSensor, InkSensor, SubstanceSensor
from ..config import INK_SENSOR_TOKEN, FLOW_SENSOR_TOKEN, SUBSTANCE_SENSOR_TOKEN
from ..light_mqtt import LightMqtt
from ..temperature_sensor import temperature_sensor
from .connect_functions import *


def run_gui(args: list = None):
    if args is None:
        args = []

    app = QApplication(args)
    app.setWindowIcon(QIcon(os.path.join(os.getcwd(), "icon.ico")))

    sched = BackgroundScheduler()
    window = MainWindow()

    flow_sensor = FlowSensor(sched, FLOW_SENSOR_TOKEN)
    ink_sensor = InkSensor(sched, INK_SENSOR_TOKEN)
    substance_sensor = SubstanceSensor(sched, SUBSTANCE_SENSOR_TOKEN)

    light_1 = LightMqtt(
        "v1/devices/me/attributes",
        "v1/devices/me/rpc/request/+",
        "XBe10xeaw8fpF6bqRr7M",
    )
    light_2 = LightMqtt(
        "v1/devices/me/attributes",
        "v1/devices/me/rpc/request/+",
        "ZsaUJIHhsCDmobiHcc3u",
    )
    light_3 = LightMqtt(
        "v1/devices/me/attributes",
        "v1/devices/me/rpc/request/+",
        "8aTocC8taPVNsYRKLjWz",
    )

    # temp_sensor_1 = temperature_sensor("Ka8qufcCQW7HhPfaH9iz", sched)
    # temp_sensor_2 = temperature_sensor("Ka8qufcCQW7HhPfaH9iz", sched)
    # temp_sensor_3 = temperature_sensor("Ka8qufcCQW7HhPfaH9iz", sched)

    # CONFIGURING FLUID WIDGETS ACTIONS
    # /////////////////////////////////////////////////////////////////////////
    window.ui.load_pages.ink_toggle.stateChanged.connect(ink_sensor.toggle)
    window.ui.load_pages.ink_color.currentTextChanged.connect(
        change_params_sensor_from_combobox(ink_sensor, window.ui.load_pages.ink_color)
    )
    window.ui.load_pages.resetInkButton.clicked.connect(
        reset_random_params_sensor(ink_sensor)
    )

    window.ui.load_pages.flow_toggle.stateChanged.connect(flow_sensor.toggle)
    window.ui.load_pages.flow_slider.sliderReleased.connect(
        change_params_sensor_from_slider(flow_sensor, window.ui.load_pages.flow_slider)
    )
    window.ui.load_pages.resetFlowButton.clicked.connect(
        reset_random_params_sensor(flow_sensor)
    )

    window.ui.load_pages.substance_toggle.stateChanged.connect(substance_sensor.toggle)
    window.ui.load_pages.substance_combo.currentTextChanged.connect(
        change_params_sensor_from_combobox(
            substance_sensor, window.ui.load_pages.substance_combo
        )
    )
    window.ui.load_pages.resetInkButton.clicked.connect(
        reset_random_params_sensor(substance_sensor)
    )

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
