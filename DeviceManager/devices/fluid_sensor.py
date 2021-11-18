from random import randint

from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.interval import IntervalTrigger


class FluidSensor:
    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        self.sched = scheduler

        if not trigger_args:
            trigger_args["seconds"] = 1
        self.default_trigger = IntervalTrigger(**trigger_args)

    def gen_data(self, *args, **kwargs) -> str:
        raise NotImplementedError()


class InkSensor(FluidSensor):
    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        super().__init__(scheduler, **trigger_args)
        self.sched.add_job(self.gen_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        return str(randint(1, 10))


class SubstanceSensor(FluidSensor):
    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        super().__init__(scheduler, **trigger_args)
        self.sched.add_job(self.gen_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        return str(randint(1, 10))


class FlowSensor(FluidSensor):
    def __init__(self, scheduler: BaseScheduler, **trigger_args) -> None:
        super().__init__(scheduler, **trigger_args)
        self.sched.add_job(self.gen_data, trigger=self.default_trigger)

    def gen_data(self) -> str:
        return str(randint(1, 10))
