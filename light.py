#!/usr/bin/env python3

import random

class Light:
    state = 2
    intensity = 100
    colorTemp = [2200, 4200]

    def __init__(self):
        self.state = random.randrange(Light.state)
        self.intensity = random.randrange(Light.intensity)
        self.colorTemp = random.randrange(Light.colorTemp[0], Light.colorTemp[1])
        if self.intensity == 0 or self.state == 0:
            self.state = 0
            self.intensity = 0
            self.colorTemp = 0


    def getAll(self):
        return self.getState(), self.getIntensity(), self.getColorTemp()
    
    def getState(self):
        if self.intensity == 0:
            return 0
        return self.state

    def getIntensity(self):
        if self.state == 0:
            return 0
        return self.intensity

    def getColorTemp(self):
        if self.state == 0:
            return 0
        return self.colorTemp

    def setState(self, value: int):
        self.state = value

    def setIntensity(self, value: int):
        self.intensity = value

    def setColorTemp(self, value: int):
        self.colorTemp = value

    def lightOn(self):
        self.setState(1)
        if self.intensity == 0:
            self.setIntensity(random.randrange(1, Light.intensity))
        if  self.colorTemp == 0:
            self.setColorTemp(random.randrange(Light.colorTemp[0], Light.colorTemp[1]))
    
    def lightOff(self):
        self.setState(0)
