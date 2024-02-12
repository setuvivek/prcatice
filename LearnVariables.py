#single value
x=5
y='john'
print(x)
print(y)
print(type(x))
print(type(y))
x1=str(5)
y1=int(3)
z1=float(3)
print(x1)
print(y1)
print(z1)

myvar='bv'
my_var='bv'
_my_var='bv'
myVar='bv'
MYVAR='bv'
myvar2='bv'

#multiple value
print()
x2,y2,z2='Chauhan','biren','v.'
print(x2)
print(y2)
print(z2)

# one value to multiple variable
print()
x3=y3=z3='Chauhan'
print(x3)
print(y3)
print(z3)

#unpack collection
print()
names = ['Chauhan','biren','V.']
x4,y4,z4=names
print(x4)
print(y4)
print(z4)

#OutPut Variables
print()
x5='python is awsome'
print(x5)

x6,y6,z6='python','is','awsome'
print(x6,y6,z6)
print(x6+y6+z6)

x7,y7=101,99
print(x7+y7)

x8,y8=101,'bv'
print(x8,y8)

#concept of global variables
print()
x9='awsome'
def Myfun():
    print("python is "+x9)
Myfun()

def myfun():
    global x10
    x10='fantastic'
myfun()
print('python is '+x10)

