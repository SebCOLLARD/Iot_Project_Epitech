import os
import sys

from apscheduler.schedulers import SchedulerAlreadyRunningError
from apscheduler.schedulers.background import BackgroundScheduler

from ..config import *
from ..devices import FlowSensor, InkSensor, SubstanceSensor, TemperatureSensor
from ..gui.main_window import MainWindow, QApplication, QIcon
from ..light_mqtt import LightMqtt
from .connect_functions import *


class QAppWithScheduler(QApplication):
    def __init__(self, args: list = None):
        super().__init__(args)
        self._sched = BackgroundScheduler()
        self.light_1 = LightMqtt(
            "v1/devices/me/attributes",
            "v1/devices/me/rpc/request/+",
            LIGHT_1_TOKEN,
        )
        self.light_2 = LightMqtt(
            "v1/devices/me/attributes",
            "v1/devices/me/rpc/request/+",
            LIGHT_2_TOKEN,
        )
        self.light_3 = LightMqtt(
            "v1/devices/me/attributes",
            "v1/devices/me/rpc/request/+",
            LIGHT_3_TOKEN,
        )

        self.flow_sensor = FlowSensor(self._sched, FLOW_SENSOR_TOKEN)
        self.ink_sensor = InkSensor(self._sched, INK_SENSOR_TOKEN)
        self.substance_sensor = SubstanceSensor(self._sched, SUBSTANCE_SENSOR_TOKEN)

        self.temp_sensor_1 = TemperatureSensor(TEMP_1_TOKEN, self._sched)
        self.temp_sensor_2 = TemperatureSensor(TEMP_2_TOKEN, self._sched)
        self.temp_sensor_3 = TemperatureSensor(TEMP_3_TOKEN, self._sched)

    def exec(self):
        try:
            self._sched.start()
        except SchedulerAlreadyRunningError:
            pass

        super().exec()

        self.light_1.stopThread()
        self.light_2.stopThread()
        self.light_3.stopThread()
        self._sched.remove_all_jobs()
        self._sched.shutdown()


def run_gui(args: list = None):
    if args is None:
        args = []

    app = QAppWithScheduler(args)
    app.setWindowIcon(QIcon(os.path.join(os.getcwd(), "icon.ico")))
    window = MainWindow()

    # CONFIGURING FLUID WIDGETS ACTIONS
    # /////////////////////////////////////////////////////////////////////////
    window.ui.load_pages.ink_toggle.stateChanged.connect(app.ink_sensor.toggle)
    window.ui.load_pages.ink_color.currentTextChanged.connect(
        change_params_sensor_from_combobox(
            app.ink_sensor, window.ui.load_pages.ink_color
        )
    )
    window.ui.load_pages.resetInkButton.clicked.connect(
        reset_random_params_sensor(app.ink_sensor)
    )

    window.ui.load_pages.flow_toggle.stateChanged.connect(app.flow_sensor.toggle)
    window.ui.load_pages.flow_slider.sliderReleased.connect(
        change_params_sensor_from_slider(
            app.flow_sensor, window.ui.load_pages.flow_slider
        )
    )
    window.ui.load_pages.resetFlowButton.clicked.connect(
        reset_random_params_sensor(app.flow_sensor)
    )

    window.ui.load_pages.substance_toggle.stateChanged.connect(
        app.substance_sensor.toggle
    )
    window.ui.load_pages.substance_combo.currentTextChanged.connect(
        change_params_sensor_from_combobox(
            app.substance_sensor, window.ui.load_pages.substance_combo
        )
    )
    window.ui.load_pages.resetInkButton.clicked.connect(
        reset_random_params_sensor(app.substance_sensor)
    )

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    print(sys.argv, type(sys.argv))
    run_gui(sys.argv)
