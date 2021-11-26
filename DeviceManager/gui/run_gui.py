import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler

from ..gui.main_window import MainWindow, QApplication, QIcon
from ..devices import FlowSensor, InkSensor, SubstanceSensor
from ..config import INK_SENSOR_TOKEN, FLOW_SENSOR_TOKEN, SUBSTANCE_SENSOR_TOKEN


def run_gui(args: list = None):
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    if args is None:
        args = []
    app = QApplication(args)
    app.setWindowIcon(QIcon(os.path.join(os.getcwd(), "icon.ico")))
    sched = BackgroundScheduler()
    flow_sensor = FlowSensor(sched, FLOW_SENSOR_TOKEN)
    ink_sensor = InkSensor(sched, INK_SENSOR_TOKEN)
    substance_sensor = SubstanceSensor(sched, SUBSTANCE_SENSOR_TOKEN)

    sched.start()
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    print(sys.argv, type(sys.argv))
    run_gui(sys.argv)
