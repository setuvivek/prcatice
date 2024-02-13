#5-print area of rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.area = 0

    def m1(self):
        print("length of rectangle" + str(self.length))
        print("width of rectangle" + str(self.width))
        print("area of rectangle" + str(self.area))

    def m2(self):
        self.area = 0.5 * self.length * self.width

obj = Rectangle(4,6)
obj.m2()
obj.m1()





#print the area of circle
# pip install python-math

# import math
# class Circle:
#     def __init__(self,rad):
#         self.rad = rad
#         self.area = 0
#     def m3(self):
#         print("the radious is" + str(self.rad))
#         print("the area is"+ str(self.area))
#
#     def m4(self):
#         self.area = math.pi * self.rad * self.rad
#
# obj2 = Circle(3)
# obj2.m4()
# obj2.m3()