#!/usr/bin/env python3

import random
import json

class LightSensor:
    _state = 2
    _intensity = 100
    _color_temp = [2200, 4200]

    def __init__(self):
        self._state = random.randrange(LightSensor._state)
        self._intensity = random.randrange(LightSensor._intensity)
        self._color_temp = random.randrange(
            LightSensor._color_temp[0], LightSensor._color_temp[1]
        )
        if self._intensity == 0 or self._state == 0:
            self._state = 0
            self._intensity = 0
            self._color_temp = 0

    def get_state(self):
        if self._intensity == 0:
            return 0
        return self._state

    def get_intensity(self):
        if self._state == 0:
            return 0
        return self._intensity

    def get_color_temp(self):
        if self._state == 0 or self._intensity == 0:
            return 0
        return self._color_temp

    def set_state(self, value: int):
        self._state = value

    def set_intensity(self, value: int):
        self._intensity = value

    def set_color_temp(self, value: int):
        self._color_temp = value

    def get_all(self):
        data : dict = {
            'state': self.get_state(),
            'intensity': self.get_intensity(),
            'color_temp': self.get_color_temp()
        }
        return json.dumps(data)

    def light_on(self):
        self._state = 1
        if self._intensity == 0:
            self.set_intensity(random.randrange(1, LightSensor._intensity))
        if self._color_temp == 0:
            self.set_color_temp(
                random.randrange(LightSensor._color_temp[0], LightSensor._color_temp[1])
            )

    def light_off(self):
        self._state = 0
