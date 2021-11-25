import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler

from DeviceManager.gui.main_window import MainWindow, QApplication, QIcon
from ..devices import FlowSensor, InkSensor, SubstanceSensor


def run_gui(args: list = None):
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    if args is None:
        args = []
    app = QApplication(args)
    app.setWindowIcon(QIcon(os.path.join(os.getcwd(), "icon.ico")))
    sched = BackgroundScheduler()
    flow_sensor = FlowSensor(sched)
    ink_sensor = InkSensor(sched)
    substance_sensor = SubstanceSensor(sched)

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
