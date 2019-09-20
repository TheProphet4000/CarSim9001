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
        self.wheels = {'frontLeft':Wheel(), 'frontRight':Wheel(), 'rearLeft':Wheel(),'rearRight':Wheel()} #laver en instans med fire hjul
        self.gears = [0,   0.8,   1,   1.4,   2.2,   3.8] # laver en instans med alle gear, disse gear bliver ganget i Gearbox
        self.clutchEngaged = False # en bool med clutch
        self.currentGear = 0 #sætter gear til 0 når man køre programmet

    def shiftUp(self):
        if self.currentGear < len(self.gears)-1 and not self.clutchEngaged: #hvis gear værdien er under det maksimale gear i gears array ->
            self.currentGear = self.currentGear + 1 # så skal der lægget 1 til current gear

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged: #hvis currentgear er større end det minimale gear i array ->
            self.currentGear = self.currentGear - 1 # så skal der trækkes 1 fra currentGear

    def rotate(self, revolutions):
        if self.clutchEngaged: #hvis clutch værdien er sand,
            for wheel in self.wheels: # så skal hvert hjul ->
                self.wheels[wheel].rotate(revolutions * self.gears[self.currentGear]) # rotere ganget med gear rationen

class Tank(object):
    def __init__(self):
        self.capacity = 100 #sætter mængten at benzin der kan være i tanken til 100, dette er en int værdi
        self.contents = 100 # samme her, dette er bare en variable der styre hvormeget der er i tanken, det er denne værdi der bliver ændret på i Engine

    def refuel (self):
        self.contents = self.capacity #en function der laver contents værdien som capacit, simulere man genopfylder tanken

    def remove(self, amount):
        self.contents = self.contents - amount   #fjerner brandstof
        if self.contents < 0: #hvis contens er minder end null, så skal den retunere null, ligemeget hvad
            self.contents = 0 # dette går at man ikke for et overflow i værdierne, så programmet crasher, eller computeren crasher.
