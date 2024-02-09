class Vehicle:

    def __init__(self, name, max_speed, mileage, color='White'):
        self.color = color
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


BUSX = Bus('School Volvo', 180, 10)
Carx = Car('Audi Q5', 240, 7)
print('Color:', BUSX.color, 'Vehicle name:', BUSX.name, 'Speed:', BUSX.max_speed, 'Mileage:', BUSX.mileage)
print('Color:', Carx.color, 'Vehicle name:', Carx.name, 'Speed:', Carx.max_speed, 'Mileage:', Carx.mileage)
