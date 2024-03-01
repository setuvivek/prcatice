# determine the person age

from datetime import date
class Person:
    def __init__(self,name,country,bdate):
        self.name = name
        self.country = country
        self.bdate = bdate

    def m2(self):
        today = date.today()
        age = today.year - self.bdate.year
        if today < date(today.year, self.bdate.month, self.bdate.day):
           age -= 1
        return age

obj = Person("hemangi","India",date(2002,12,22))

print("person name is ", obj.name)
print("person country is ", obj.country)
print("person bdate is ", obj.bdate)
print("person age is ", obj.m2())