from Car import *


class New(Car):
    self = ''

    def __init__(self, started, speed):
        self = 'Ford'
        self.speed = 0
        self.started = True


car = New.__init__()
print('the new car is ' + str(New.isStarted(car)))
