import sys

from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup()

    def setup(self):
        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle("Window Example")
        self.show()


def run_gui(args: list = None):
    app = QApplication(args or [])
    window = Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui([])
