class Person:
    def __init__(self):
        # data members (instance variables)
        self.name = input("enter name :")
        self.sex =  input("enter sex : ")
        self.profession = input("enter profession : ")
    # name = input("enter name :")
    # sex = input("enter sex : ")
    # profession =  input("enter profession : ")
    def show(self):
        print('Name:',self.name, 'Sex:', self.sex, 'Profession:', self.profession)
    def work(self):
        print(self.name, 'working as a', self.profession)

jessa = Person()
jessa.show()



#single inherittance
class Student:
    def show(self):
        print("i am student")
class Tacher(Student):
    def shows(self):
        print("i am teacher")
s1 = Tacher()
s1.show()
s1.shows()


#multiple inheritance
class Stu:
    def __init__(self):
        self.name = input("enter name : ")
        self.address= input("enter address : ")
class Show1:
    def __init__(self):
        self.name = None
    def showd(self):
        print(self.name)
class Show2:
    def __init__(self):
        self.profession = None
    def showf(self):
        print(self.address)
class Show(Stu,Show1,Show2):
    def pri(self):
        print(self.name, " is  available at" , self.address)
s = Show()
s.pri()

# example of hybrid inheritance
class Stu:
    def __init__(self):
        # print("hello")
        self.name = input("enter name : ")
        self.city = input ("enter city :  ")
        self.country = input("enter country :")
class A(Stu):
    def d(self):
        # print("Show1")
        print(self.name)
class B(Stu):
    def e(self):
        # print("Show2")
        print(self.city)
class Last(A,B):
    def diss(self):
        # print("SHOW")
        print(self.name ," stable in ", self.city)
        print(self.city , " is in ", self.country)

s1 = Last()
s1.d()
s1.e()
s1.diss()


# example of multilevel inheritance
class St:
    def __init__(self):
        print("hi")
class teacher(St):
    def pr(self):
        print("i am teacher")
class prof(teacher):
    def pri(self):
        print(" i am proffesor")

s1 = prof()
s1.pri()
s1.pr()

# example of hierarchical inheritance
class Doc:
    def __init__(self):
        print("hi")

class Nur(Doc):
    def ou(self):
        print("nurse")
class Pune(Doc):
    def out(self):
        print("pune")
class Pat(Doc):
    def outp(self):
        print("Pat")

s1 = Pat()
s1.outp()
s2 = Nur()
s2.ou()

class Vehicle:
    # constructor
    def __init__(self):
        self.name = input("enter name : " )
        self.college = input("enter college name : ")
    def show(self):
        print(self.name , " is student of ", self.college , " college ")
# 1st objecy
s1 = Vehicle()
s1.show()


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
