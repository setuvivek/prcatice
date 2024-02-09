#tuple in python
a = ("a","b","c","d","e","f","g")
print(type(a))
print(len(a))
#unpacking tuple
a = ("karan" , 15 , 2020)
(name,age,year)= a
print(name)
print(age)
print(year)
j,k, *l = ("karan", "brother", 12,34,67)
print(j)
print(k)
print(l)

k = ("a","b","c")
for x in k:
    print(k)

tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
print(tup1 + tup2)
print(tup1*3)
print(tup2*2)

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

list = ["even number" if i%2==0 else "odd number" for i in range(8)]
print(list)

list = [num for num in range(100)
       if num % 5 == 0 if num % 10 == 0]
print(list)

# Getting square of number from 1 to 10
squares = [n ** 2 for n in range(1, 11)]
# Display square of even numbers
print(squares)

List = [string[::-1] for string in ("kinnari","Sanjaybhai","tank")]
print(List)

#dictionary
dict = {"A":10 ,"b":20, "C":30, "d":40}
print(dict)
print(type(dict))
print(len(dict))
dict2 = {"a":22 , "b":45, "c":[7,8,9]}
print(dict2)
print(type(dict2))
x = dict.keys()
print(x)
y= dict.values()
print(y)
r = dict2.keys()
print(r)
t = dict2.keys()
print(t)
u = dict.items()
print(u)
v = dict2.items()
print(v)
dict["A"] = 50
print(dict)
dict2["c"] = [70,80,90]
print(dict2)
dict.update({"C":44})
dict.update({"d":77})
print(dict)
dict.popitem()
print(dict)
del dict["C"]
print(dict)
for x in dict:
    print(x)
for i in dict:
    print(i,":",dict[i])
for j in dict2:
    print(j,":",dict2[j])
state = {"m":"mumbai", "g":"gujarat", "r":"rajashathan" , "d":"delhi"}
for x in state:
    print(f'the state,{x},is,{state[x]}')
for x in dict.values():
    print(x)
for x,y in dict.items():
    print(x,y)
dict3 = dict.copy()
print(dict3)










