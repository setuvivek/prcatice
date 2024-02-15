for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


val1=  20
val2=  11
print(val1/val2)
print(val1//val2)

a=10
b=1
# Subtract and assign value
b-=a
print("Subtract and assign value :", b)

g=3
h=6
k=g-h
print(k)
a = 3
b = 5
# a = a ** b
a **= b
# Output
print(a)

k=20
j=50
print(k>j)

s=50
d=60
print(s and d )
print(s or d)
print(not d)

a = 20
b = 70

if ( a is b ):
   print("Line 1 - a and b have same identity")
else:
   print("Line 1 - a and b do not have same identity")


# membership operator in Python
# using "in" operator
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is a fruit!")
# using "not in" operator
if "orange" not in fruits:
    print("Yes, orange is not in the list of fruits")


# membership operator in Python
# using "in" operator
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes")
# using "not in" operator
if "orange" in fruits:
    print("available")

if "orange" not in fruits:
    print("not available")


    x = 24

    y = 20

    list = [10, 20, 30, 40, 50]

    if (x not in list):

       print("x is NOT present in given list")

    else:

        print("x is present in given list")

    if (y in list):

       print("y is present in given list")

    else:

        print("y is NOT present in given list")

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])


for i in range(10):

    print(i, end = " ")
print()

sum = 0
for i in range(1, 10):
   sum = sum + i
print("Sum of first 10 numbers :", sum)

numbers = [12, 13, 14,]
doubled = [x *2 for x in numbers]
print(doubled)


numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)


k=18
if (k>40):
    print("THank you")
else:
   print("welcome")

k = 55
if (k>50):
    print("K is greater than 50")
else:
    print("k is smaller than 50")



marks = int(input("enter mark : "))
if (marks<=20):
    print("fail")
if (marks<=40 and marks>20):
    print("low result")
if(marks<=60 and marks>40):
    print("average result")
if(marks<=80 and marks>60):
    print("result is good")
if(marks<=100 and marks>80):
    print("extremly very good result")


marks = int(input("enter marks : "))
if(marks>=80):
    print("very gooood")
elif(marks>=60 and marks<80):
    print("gooood")
elif(marks>=40 and marks<60):
    print("average")
elif(marks>=20 and  marks<40):
    print("poor")
elif(marks<20):
    print("fail")

j = 0
while j <7:
    print(j)
    j += 1
c = 0
while c<5: c+=1 ; print("Thank you")


k = "Kinnari"
i = 0
while len(k) > i:
    i += 1
    print(k)

a = ["a","b","c","d","e","f"]
for x in a:
    print(a)

list = ["apple", "banana", "orqnge", "mango"]
list.append("kiwi")
print(list)
list.insert(2 ,"cherry")
print(list)


l1 = ["a","b","c","d","d"]
l2 = ["e", "f", "g"]
l1.extend(l2)
print(l1)
l1.pop()
print(l1)
l1.remove("c")
print(l1)
del list[0]
print(l1)

list.sort()
print(list)

a = { "a", "b","c","d","e","f","g","a"}
print(type(a))
print(len(a))
a.add("h")
print(a)
b = {"i","j","k","l","m","n"}
a.update(b)
print(a)

a.update(list)
print(a)

a.remove("a")
print(a)
a.add("a")
print(a)
a.discard("k")
print(a)

set3 = a.union(b)
print(set3)
set3 = a.intersection(b)
print(set3)
set3 = a.difference(b)
print(set3)
set3 = a.update(b)
print(a)

set1 = {1,2,3,4,5}
set2 = {6,7,8,9}
set3 = set1.union(set2)
print(set3)
set4 = set1.difference(set2)
print(set4)
set5 = set1.intersection(set2)
print(set5)
set6 = set1.difference_update(set2)
print(set6)
set7 = set1.intersection_update(set2)
print(set7)
set8 = set1.symmetric_difference(set2)
print(set8)
set9 = set1.symmetric_difference_update(set2)
print(set9)






