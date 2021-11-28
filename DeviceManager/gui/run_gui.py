import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerAlreadyRunningError

from ..gui.main_window import MainWindow, QApplication, QIcon
from ..devices import FlowSensor, InkSensor, SubstanceSensor
from ..config import INK_SENSOR_TOKEN, FLOW_SENSOR_TOKEN, SUBSTANCE_SENSOR_TOKEN
from ..light_mqtt import LightMqtt
from ..temperature_sensor import temperature_sensor
from .connect_functions import *


class QAppWithScheduler(QApplication):
    def __init__(self, sched: BackgroundScheduler, args: list = None):
        super().__init__(args)
        self._sched = sched
        try:
            self._sched.start()
        except SchedulerAlreadyRunningError:
            pass
        # self.light_1 = LightMqtt(
        #     "v1/devices/me/attributes",
        #     "v1/devices/me/rpc/request/+",
        #     "XBe10xeaw8fpF6bqRr7M",
        # )
        # self.light_2 = LightMqtt(
        #     "v1/devices/me/attributes",
        #     "v1/devices/me/rpc/request/+",
        #     "ZsaUJIHhsCDmobiHcc3u",
        # )
        # self.light_3 = LightMqtt(
        #     "v1/devices/me/attributes",
        #     "v1/devices/me/rpc/request/+",
        #     "8aTocC8taPVNsYRKLjWz",
        # )

        # self.flow_sensor = FlowSensor(sched, FLOW_SENSOR_TOKEN)
        # self.ink_sensor = InkSensor(sched, INK_SENSOR_TOKEN)
        # self.substance_sensor = SubstanceSensor(sched, SUBSTANCE_SENSOR_TOKEN)

        # self.temp_sensor_1 = temperature_sensor("ltwVlFbm8pJh02rq0qak", sched)
        # self.temp_sensor_2 = temperature_sensor("IF58gDIaojWCMZgwcTnH", sched)
        # self.temp_sensor_3 = temperature_sensor("5Q6PTQtY8pLaq7oFosqf", sched)

    def __del__(self):
        # self.light_1.stopThread()
        # self.light_2.stopThread()
        # self.light_3.stopThread()
        self._sched.remove_all_jobs()
        self._sched.shutdown()


def run_gui(args: list = None):
    if args is None:
        args = []

    app = QAppWithScheduler(BackgroundScheduler(), args)
    app.setWindowIcon(QIcon(os.path.join(os.getcwd(), "icon.ico")))
    window = MainWindow()

    # CONFIGURING FLUID WIDGETS ACTIONS
    # /////////////////////////////////////////////////////////////////////////
    # window.ui.load_pages.ink_toggle.stateChanged.connect(app.ink_sensor.toggle)
    # window.ui.load_pages.ink_color.currentTextChanged.connect(
    #     change_params_sensor_from_combobox(
    #         app.ink_sensor, window.ui.load_pages.ink_color
    #     )
    # )
    # window.ui.load_pages.resetInkButton.clicked.connect(
    #     reset_random_params_sensor(app.ink_sensor)
    # )

    # window.ui.load_pages.flow_toggle.stateChanged.connect(app.flow_sensor.toggle)
    # window.ui.load_pages.flow_slider.sliderReleased.connect(
    #     change_params_sensor_from_slider(
    #         app.flow_sensor, window.ui.load_pages.flow_slider
    #     )
    # )
    # window.ui.load_pages.resetFlowButton.clicked.connect(
    #     reset_random_params_sensor(app.flow_sensor)
    # )

    # window.ui.load_pages.substance_toggle.stateChanged.connect(
    #     app.substance_sensor.toggle
    # )
    # window.ui.load_pages.substance_combo.currentTextChanged.connect(
    #     change_params_sensor_from_combobox(
    #         app.substance_sensor, window.ui.load_pages.substance_combo
    #     )
    # )
    # window.ui.load_pages.resetInkButton.clicked.connect(
    #     reset_random_params_sensor(app.substance_sensor)
    # )

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    print(sys.argv, type(sys.argv))
    run_gui(sys.argv)
