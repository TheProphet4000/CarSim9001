from random import randint

class Car(object):
    def __init__(self):
        self.theEngine; #skal kalde Engine
        self.updateModel #skal kalde updatemodel på engine

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0,360)

    def rotate(self,revolutions):
        self.orientation = (self.orientation+(revolutions*360))%360

class Engine(object):
    def __init__(self):
        self.throttlePosition[0,1] #speeder 1 eller 0
        self.theGearbox = Gearbox(); #skal indholde en instats af Gearbox
        self.currentRpm = 0;
        self.consumptionConstant = 10,0;
        self.maxRpm = 100;
        self.theTank = Tank(); # skal indenholde instats af Tank
        self.updateModel #skal regne det hele og pakke det til car (DT er deltaTime)

        #Skal gange throttlePosition*maxRpm =currentRpm
        #skal bruge benzin  remove (på tank)   currentRpm*consumptionConstant
        #skal kalde rotate(theGearbox på currentRpm*(dt/60) som parameter)

class Gearbox(object):
    def __init__(self):
        self.wheels = {'frontLeft':Wheel(), 'frontRight':Wheel(), 'rearLeft':Wheel(),'rearRight':Wheel()}
        self.gears = [0,   0.8,   1,   1.4,   2.2,   3.8]
        self.clutchEngaged = False
        self.currentGear = 0

    def shiftUp(self):
        if self.currentGear < len(self.gears)-1 and not self.clutchEngaged:
            self.currentGear = self.currentGear + 1

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged:
            self.currentGear = self.currentGear - 1

    def rotate(self, revolutions):
        if self.clutchEngaged:
            for wheel in self.wheels:
                self.wheels[wheel].rotate(revolutions * self.gears[self.currentGear])

class Tank(object):
    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def refuel (self):
        self.contents = self.capacity

    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0
