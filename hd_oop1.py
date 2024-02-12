#3- create a child class bus and inherit all the properties and variables from vehicle


class Vehicle:
    def __init__(self,max_speed,milege):
        self.max_speed = max_speed
        self.milege = milege

    def m1(self):
        print("vehicla max_speed ", self.max_speed)
        print("vehicle milege",self.milege)
obj = Vehicle(60,70)


class Bus(Vehicle):
    def m2(self):
        print("parent class called")

obj1 = Bus(66,77)
obj1.m1()