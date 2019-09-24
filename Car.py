
class Vehicle(object):
    """docstring"""
    speed = 0

    def __init__(self, color, doors, tires, vtype, speed):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype
        self.speed = speed

    def brake(self):
        """
        Stop the car
        """
        Vehicle.speed = 0
        return "%s braking" % Vehicle.speed

    def drive(self, speed):
        """
        Drive the car
        """
        Vehicle.speed += 5
        return "I'm driving a %s %s! %s" % (self.color, self.vtype, Vehicle.speed)


if __name__ == "__main__":
    truck = Vehicle("red", 3, 6, "truck", str(Vehicle.speed))
    print(truck.drive(Vehicle.speed))
    print(truck.brake())

    car = Vehicle("blue", 5, 4, "car", str(Vehicle.speed))
    print(car.brake())
    print(car.drive(Vehicle.speed))



