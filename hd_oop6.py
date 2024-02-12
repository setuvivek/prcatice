#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
class Vehicle:
    color = "white"
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

obj = Vehicle("palak",60,70)

class Car(Vehicle):
    pass
obj1 = Car("Sarthak",80,20)

class Bus(Vehicle):
    pass
obj2 = Bus("Hemangi",90,10)

print("Color:",obj1.color,"Name:",obj1.name,"Speed:",obj1.max_speed,"milege:",obj1.mileage)
print("Color:",obj2.color,"Name:",obj2.name,"Speed:",obj2.max_speed,"milege:",obj2.mileage)