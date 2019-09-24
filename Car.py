
class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype, speed):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype
        self.speed = 0

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype

    def drive(self,speed):
        """
        Drive the car
        """
        speed +=5
        return "I'm driving a %s %s! %s" % (self.color, self.vtype,self.speed)


if __name__ == "__main__":
    truck = Vehicle("red", 3, 6, "truck", speed)
    print(truck.drive())
    print(truck.brake())

    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())



