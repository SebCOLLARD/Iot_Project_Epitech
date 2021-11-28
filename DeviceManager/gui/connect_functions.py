from ..devices.fluid_sensor import FluidSensor
from PySide6.QtWidgets import QComboBox, QSlider


def change_params_sensor_from_combobox(sensor: FluidSensor, combo: QComboBox):
    """
    Factory to create calls to the sensor's ``change_job_params` method with a QComboBox' current text.

    Params:
    - sensor (FluidSensor): the FluidSensor instance in which to change the job's params
    - combo (QComboBox): the QComboBox widget from which to get the data

    Returns a callable.
    """

    def wrapper():
        sensor.change_job_params(sensor.data_from_values(combo.currentText()))

    return wrapper


def change_params_sensor_from_slider(sensor: FluidSensor, slider: QSlider):
    """
    Factory to create calls to the sensor's ``change_job_params` method with a QSlider's current value.

    Params:
    - sensor (FluidSensor): the FluidSensor instance in which to change the job's params
    - slider (QSlider): the QComboBox widget from which to get the data

    Returns a callable.
    """

    def wrapper():
        sensor.change_job_params(sensor.data_from_values(slider.value()))

    return wrapper


def reset_random_params_sensor(sensor: FluidSensor):
    """
    Factory to create calls to the sensor's ``change_job_params` method without parameter, to return to default random generation.

    Params:
    - sensor (FluidSensor): the FluidSensor instance in which to reset the job's param.

    Returns a callable.
    """

    def wrapper():
        sensor.change_job_params()

    return wrapper
