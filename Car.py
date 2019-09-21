class Car:
#Created by Jorge
    def __init__(self,speed, started):

        self.speed = 0
        self.started = False

    def start(self,started, speed):
        self.started = True
        self.speed= 0

    def isStarted(self):
        return(Car.started)





