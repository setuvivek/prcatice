#int
x,y,z=2,2344432432,-1233212
print(x,'\n',y,'\n',z)

#float
print()
x1,y1,z1,a,b,c=1.21,1.0,-23.23,32e1,122e2,-23.32e22
print(x1,'\n',y1,'\n',z1,'\n',a,'\n',b,'\n',c)

#convert one type to another
x2,y2,z2=1,2.3,32j
print(type(x2))
print(type(y2))
print(type(z2))

x2=float(x2)
y2=int(y2)
z2=complex(x2)
print()
print(type(x2))
print(type(y2))
print(type(z2))

#random number
print()
import random
print(random.randrange(1,5))