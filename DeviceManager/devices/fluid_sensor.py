import json
from logging import debug
from random import choice, uniform
from typing import Any

from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.interval import IntervalTrigger

from ..protocols import CoapThingsboardClient


class FluidSensor:
    """
    Abstract class representing all fluid-related IoT sensors.
    """

    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
        """
        Params:
        - scheduler (BaseScheduler): An APScheduler scheduler class of any kind
        - token (str): Thingsboard device access token
        - trigger_params: Parameters for the IntervalTrigger object used in the scheduler. Default to seconds=1
        """
        self.sched = scheduler
        self.client = CoapThingsboardClient()
        self.token = token
        self.enabled = True

        if not trigger_args:
            trigger_args["seconds"] = 1
        self.default_trigger = IntervalTrigger(**trigger_args)

    def gen_data(self) -> str:
        """
        Returns a JSON payload with random values.
        """
        raise NotImplementedError()

    def data_from_values(self, *args) -> str:
        """
        Returns a JSON payload from given values.
        """
        raise NotImplementedError()

    def get_callback(self):
        """
        Callback factory for the CoAP protocol calls.
        """

        def cb(*args):
            debug("Inside callback. Received: " + str(args))

        return cb

    def _check_running(func):
        """
        Decorator to ensure `func` is run only if the sensor is enabled.
        """

        def wrapper(self, *args, **kwargs) -> Any:
            if self.enabled:
                return func(self, *args, **kwargs)
            else:
                return None

        return wrapper

    @_check_running
    def send_data(self, data: str = None):
        """
        Send data to the Thingsboard server.

        Params:
        - data (str): A JSON body to send to Thingsboard. If None or empty, random data is generated.
        """
        if data is None or data == "":
            data = self.gen_data()
        self.client.post(self.token, data, self.get_callback(), timeout=10)

    def change_job_params(self, new_json=None):
        """
        Change JSON values sent to server.
        If `new_json` is not provided, it defaults back to random generation.
        """
        try:
            trigger = self.job.trigger
        except ReferenceError:
            trigger = self.default_trigger
        else:
            self.sched.remove_job(self.job.id)
        finally:
            self.job = self.sched.add_job(
                self.send_data, trigger=trigger, args=[new_json]
            )

    def toggle(self) -> bool:
        """
        Toggle the sensor.
        Returns wether the toggling succeeded.
        """
        try:
            if self.enabled:
                self.job = self.sched.pause_job(self.job.id)
            else:
                self.job = self.sched.resume_job(self.job.id)
        except ReferenceError:
            return False
        else:
            self.enabled = not self.enabled
            return True


class InkSensor(FluidSensor):
    """
    Represents an ink color sensor.
    """

    _colors = ["cyan", "magenta", "yellow", "black", "red", "blue", "green"]

    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
        super().__init__(scheduler, token, **trigger_args)
        self.job = self.sched.add_job(self.send_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        payload = {"color": choice(InkSensor._colors)}
        debug(payload)
        return json.dumps(payload)

    def data_from_values(self, color: str = None) -> str:
        if not color:
            return None
        payload = {"color": color}
        debug(payload)
        return json.dumps(payload)


class SubstanceSensor(FluidSensor):
    """
    Represents a substance kind sensor.
    """

    _substances = ["alcohol", "water", "oil"]

    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
        super().__init__(scheduler, token, **trigger_args)
        self.job = self.sched.add_job(self.send_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        payload = {"substance": choice(SubstanceSensor._substances)}
        debug(payload)
        return json.dumps(payload)

    def data_from_values(self, substance: str = None) -> str:
        if not substance:
            return None
        payload = {"substance": substance}
        debug(payload)
        return json.dumps(payload)


class FlowSensor(FluidSensor):
    """
    Represents a flow sensor.
    """

    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
        super().__init__(scheduler, token, **trigger_args)
        self.job = self.sched.add_job(self.send_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        payload = {"flow_in_ml_per_s": round(uniform(-10, 150), 3)}
        debug(payload)
        return json.dumps(payload)

    def data_from_values(self, flow: float = None) -> str:
        if not flow and flow != 0:
            return None
        payload = {"flow_in_ml_per_s": flow}
        debug(payload)
        return json.dumps(payload)
