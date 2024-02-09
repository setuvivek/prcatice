class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


BUSX = Bus('School Volvo', 120, 10)
print('Vehicle Name :', BUSX.name, 'Speed :', BUSX.max_speed, 'Mileage :', BUSX.mileage)
