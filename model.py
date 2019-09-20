from random import randint

class Car(object): # en class så man næmmere
    def __init__(self): #initiere Car, så man bare skal skrive self, og ikke hele class. Så kan man også kalde childs fra andree classes
        self.theEngine = Engine() #kalder Engine

    def updateModel(self,dt):
        self.theEngine.updateModel(dt) #updatere Engine

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0,360) #sætter orientation til et tilfældigt int mellem 0, og 360

    def rotate(self,revolutions):
        self.orientation = (self.orientation+(revolutions*360))%360 # rotere hjulet

class Engine(object):
    def __init__(self):
        self.throttlePosition = 0 #speeder 1 eller 0
        self.theGearbox = Gearbox()#skal indholde en instats af Gearbox
        self.currentRpm = 0 #sætter default til 0
        self.consumptionConstant = 0.0025 #giver en konstatnt som bliver fjernet for Tank hver update
        self.maxRpm = 100 #sætter maximun hastighed på Engine
        self.theTank = Tank() # skal indenholde instats af Tank

    def updateModel(self , dt): # denne funktion styre alt i bilen, engine, tank, alt.... mere eller mindre kernen i koden.
        if self.theTank.contents > 0: # hvis tankens inhold er større end null, så skal bilkoden kunne køre
            self.currentRpm = self.throttlePosition * self.maxRpm #sætter currentRpm til thruttleposition ganget med maxRpm... altså enten er det maxRpm, ellers er det null
            self.theTank.remove(self.currentRpm * self.consumptionConstant) # fjerner tank indhold med currentRpm*consumptionConstant... altså bilens brandstof forbrug
            self.theGearbox.rotate(self.currentRpm * (dt / 60)) #rotere gearbox med hvormange gange computeren updatere i minutet
        else:
            self.currentRpm = 0 #hvis der ikke er noget brandstof, set currentRpm til null

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
