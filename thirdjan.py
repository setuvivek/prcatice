#break statement used for terminate the loop or statement
s ="kinnari"

for letter in s:
    print(letter)
    if letter == "n":
        break
print("exit from loop")

#continue statement is oppositer from break
#focus on execute next iteration
for i in range(1,16):
    if i == 5:
        continue
    else:
        print(i, end=" ")
print()

r = "kinnari"
for i in r:
    if i == "n":
        continue
    else:
        print(i , end=" ")

print()

#pass statement used for nothing.
#it is just like null
d = "kinnari"
for i in d:
    if i == "n":
        pass
    else:
        print(i, end=" ")
print()


#list in python
list1 = [ "a","b", "c", "d","i","j","k","l"]
list2 = ["e", "f", "g" ,"h"]
print(type(list1))
print(type(list2))
print(list1[3])
print(list2[2])
print(list1[1:4])
print(list1[2:])
print(list1[:4])
if "a" in list1:
    print("a is present in list")
if "b" in list1:
    print("b is present in list")
if "f" in list2:
    print("f is present in list2")
list1.append("m")
print(list1)
list1.insert(2 , "n")
print(list1)
list2.insert(4 , "o")
print(list2)
list1.remove("a")
list2.remove("e")
print(list1)
print(list2)
list1.pop()
print(list1)
i = 0
while i < len(list1):
    print(list1[i],end=" ")
    i = i+1
print()
for i in range(len(list1)):
    print(list1[i] , end=" ")
print()
[print(x, end=" ") for x in list2]
print()
[print(x, end=" ") for x in list1]
print()
list3 = list1+list2
print(list3)
list1.extend(list2)
print(list1)



