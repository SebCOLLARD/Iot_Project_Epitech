from random import choice, uniform
from logging import debug
import json

from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.interval import IntervalTrigger

from ..protocols import CoapThingsboardClient
from ..config import INK_SENSOR_TOKEN, FLOW_SENSOR_TOKEN, SUBSTANCE_SENSOR_TOKEN


class FluidSensor:
    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        self.sched = scheduler
        self.client = CoapThingsboardClient()

        if not trigger_args:
            trigger_args["seconds"] = 1
        self.default_trigger = IntervalTrigger(**trigger_args)

    def gen_data(self, *args, **kwargs) -> str:
        """
        Returns a JSON payload.
        """
        raise NotImplementedError()

    def get_callback(self):
        def cb(*args):
            print(*args)

        return cb

    def send_data(self, access_token):
        self.client.post(access_token, self.gen_data(), self.get_callback(), timeout=10)


class InkSensor(FluidSensor):
    _colors = ["cyan", "magenta", "yellow", "black", "red", "blue", "green"]

    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        super().__init__(scheduler, **trigger_args)
        self.job = self.sched.add_job(
            self.send_data, args=[INK_SENSOR_TOKEN], trigger=self.default_trigger
        )

    def gen_data(self) -> str:
        payload = {"color": choice(InkSensor._colors)}
        debug(payload)
        return json.dumps(payload)


class SubstanceSensor(FluidSensor):
    _substances = ["alcohol", "water", "oil"]

    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        super().__init__(scheduler, **trigger_args)
        self.job = self.sched.add_job(
            self.send_data, args=[SUBSTANCE_SENSOR_TOKEN], trigger=self.default_trigger
        )

    def gen_data(self) -> str:
        payload = {"substance": choice(SubstanceSensor._substances)}
        debug(payload)
        return json.dumps(payload)


class FlowSensor(FluidSensor):
    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        super().__init__(scheduler, **trigger_args)
        self.job = self.sched.add_job(
            self.send_data, args=[FLOW_SENSOR_TOKEN], trigger=self.default_trigger
        )

    def gen_data(self) -> str:
        payload = {"flow_in_ml_per_s": round(uniform(-200, 1500), 3)}
        debug(payload)
        return json.dumps(payload)
