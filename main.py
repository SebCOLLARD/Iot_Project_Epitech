#!/bin/usr/env python3

import argparse
import sys

from DeviceManager import run_gui

parser = argparse.ArgumentParser(
    prog="IoT Device Manager (CLI)",
    description="This is the Command Line interface version of the IoT Device Manager.",
    epilog="This is a 4th year Epitech Global Nomad Track project, promotion 2023.",
)
parser.add_argument("-n", "--no-gui", action="store_true")
args = parser.parse_args()

if not args.no_gui:
    run_gui(sys.argv)
else:
    print("Launched without GUI, not supported for the moment.")
