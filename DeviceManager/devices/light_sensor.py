#!/usr/bin/env python3

import random
import json

class LightSensor:
    """
    Simulated IoT sensor for light. 
    """

    _state = 2
    _intensity = 100
    _color_temp = [2200, 4200]

    def __init__(self):
        """
        Initialise the light state, intensity and color temperature using random.
        """
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
        """
        Get the state of electricity.
        """
        return self._state

    def get_intensity(self):
        """
        Get the light intensity.
        """
        if self._state == 0:
            return 0
        return self._intensity

    def get_color_temp(self):
        """
        Get the light color temperature.
        """
        if self._state == 0 or self._intensity == 0:
            return 0
        return self._color_temp

    def set_state(self, value: int):
        """
        Set the state of electricity.
        """
        self._state = value

    def set_intensity(self, value: int):
        """
        Set the light intensity.
        """
        self._intensity = value

    def set_color_temp(self, value: int):
        """
        Set the light color temperature.
        """
        self._color_temp = value

    def get_all(self):
        """
        led = When the intensity is at 0 the LED turns off. Is not depending off the state.
        Return a JSON containing the light data.  
        """
        if self.get_state() == 0:
            led = 0
        elif self.get_state() == 1 and self.get_intensity() == 0:
            led = 0
        else:
            led = 1
        data : dict = {
            'state': self.get_state(),
            'led': led,
            'intensity': self.get_intensity(),
            'color_temp': self.get_color_temp()
        }
        return json.dumps(data)

    def light_on(self):
        """
        Turn on the light, and set the intensity and the color temperature.
        """
        self._state = 1
        if self._intensity == 0:
            self.set_intensity(random.randrange(1, LightSensor._intensity))
        if self._color_temp == 0:
            self.set_color_temp(
                random.randrange(LightSensor._color_temp[0], LightSensor._color_temp[1])
            )

    def light_off(self):
        """
        Turn off the light from the switch.
        """
        self._state = 0
