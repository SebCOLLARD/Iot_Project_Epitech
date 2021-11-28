from ..devices.fluid_sensor import FluidSensor
from PySide6.QtWidgets import QComboBox, QSlider


def change_params_sensor_from_combobox(sensor: FluidSensor, combo: QComboBox):
    def wrapper():
        sensor.change_job_params(sensor.data_from_values(combo.currentText()))

    return wrapper


def change_params_sensor_from_slider(sensor: FluidSensor, slider: QSlider):
    def wrapper():
        sensor.change_job_params(sensor.data_from_values(slider.value()))

    return wrapper


def reset_random_params_sensor(sensor: FluidSensor):
    def wrapper():
        sensor.change_job_params()

    return wrapper
