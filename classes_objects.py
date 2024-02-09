#Create a Class
class MyClass:
    x = 5
#Create Object
p1 = MyClass()
print(p1.x)

#The __init__() Function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person('riken','22')
print(p1.name)
print(p1.age)

#The __str__() Function
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1=person("riken",22)
print(p1)

#Object Methods
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is" " " + self.name)
p1 = person("john",36)
p1.myfunc()


#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)


#Delete Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)

#Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
print(p1)

#The pass Statement
class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement