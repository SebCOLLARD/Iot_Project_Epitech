from os import getcwd
from os.path import abspath, dirname, join

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {"include_files": ["./PyOneDark_settings.json", "./icon.ico"]}

import sys

base = "Win32GUI" if sys.platform == "win32" else None
bin_name = "iot_device_manager.exe" if sys.platform == "win32" else "iot_device_manager"

executables = [Executable("main.py", base=base, target_name=bin_name, icon="icon.ico")]

setup(
    name="IoTDeviceManager",
    version="0.1",
    description="This is a graphical interface for the IoTDeviceManager of the IoT Project for Epitech 4th year Global Nomad Track, 2021-2022 (promotion 2023).",
    options={"build_exe": build_options},
    executables=executables,
)
