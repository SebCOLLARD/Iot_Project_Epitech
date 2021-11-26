from random import choice, uniform
from logging import debug
from typing import Any
import json

from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.job import Job

from ..protocols import CoapThingsboardClient


class FluidSensor:
    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
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
        Returns a JSON payload from given dict (or keyword arguments).
        """
        raise NotImplementedError()

    def get_callback(self):
        def cb(*args):
            debug("Inside callback. Received: {}", *args)

        return cb

    def check_running(self, func):
        def wrapper(*args, **kwargs) -> Any | None:
            if self.enabled:
                return func(*args, **kwargs)
            else:
                return None

        return wrapper

    @check_running
    def send_data(self, data=None):
        if data is None:
            data = self.gen_data()
        self.client.post(self.token, data, self.get_callback(), timeout=10)

    @check_running
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
            self.sched.remove_job(self.job)
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
    _colors = ["cyan", "magenta", "yellow", "black", "red", "blue", "green"]

    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
        super().__init__(scheduler, token, **trigger_args)
        self.job = self.sched.add_job(self.send_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        payload = {"color": choice(InkSensor._colors)}
        debug(payload)
        return json.dumps(payload)

    def data_from_values(self, color: str) -> str:
        payload = {"color": color}
        debug(payload)
        return json.dumps(payload)


class SubstanceSensor(FluidSensor):
    _substances = ["alcohol", "water", "oil"]

    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
        super().__init__(scheduler, token, **trigger_args)
        self.job = self.sched.add_job(self.send_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        payload = {"substance": choice(SubstanceSensor._substances)}
        debug(payload)
        return json.dumps(payload)

    def data_from_values(self, substance: str) -> str:
        payload = {"substance": substance}
        debug(payload)
        return json.dumps(payload)


class FlowSensor(FluidSensor):
    def __init__(self, scheduler: BaseScheduler, token: str, **trigger_args) -> None:
        super().__init__(scheduler, token, **trigger_args)
        self.job = self.sched.add_job(self.send_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        payload = {"flow_in_ml_per_s": round(uniform(-200, 1500), 3)}
        debug(payload)
        return json.dumps(payload)

    def data_from_values(self, flow: float) -> str:
        payload = {"flow_in_ml_per_s": flow}
        debug(payload)
        return json.dumps(payload)
