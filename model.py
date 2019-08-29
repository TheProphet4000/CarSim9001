from random import randint

class Car(object):
    pass

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0,360)

    def rotate(self,revolutions):
        self.orientation = (self.orientation+(revolutions*360))%360


class Engine(object):
    pass

class Gearbox(object):
    pass

class Tank(object):
    def _init_(self):
        self.capacity = 100
        self.contents = 100

    def refuel (self):
        self.contents = self.capacity

    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0
