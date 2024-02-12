MyList = ['cricket', 'carrom', 'chess', 'wallyball']
print(MyList)
print(MyList[3])
MyList[2] = "Bike Race"
print(MyList)
print(len(MyList))

print('Type Of List')
print()
l1 = ['this', 'is', 'str', 'list']
l2 = [1, 2, 3, 4, 5, 6]
l3 = [True, False, False, False, True]
l4 = ['hii', 23, 22, 22, True, 'okey']

print(type(l1))
print(type(l2))
print(type(l3))
print(type(l4))

print('list constructor')
print()
list1 = list(("Hello", "How", "Are", "You"))
print(list1)

print('Access from list')
print()
print(list1[1])
print(list1[-1])
print(list1[1:3])
print(list1[2:])
print(list1[:3])
print(list1[-4:-1])
print(list1[::-1])
print(list1[:-3:-1])
list1[1:3] = 'v', 'a'
print(list1)

print('Methods oprations')
print('upadte')
MyList[1] = "Bike"
print(MyList)

print('insert')
list1 = list(("Hello", "How", "Are", "You"))
list1.insert(1, "yes")
print(list1)
list1.append("yes")
print(list1)
list1.extend(MyList)

print('delete')
print(list1)
list1.remove("yes")
print(list1)
list1.pop(3)
print(list1)
list1.pop()
print(list1)
del list1[1]
print(list1)
list1.clear()
print(list1)
del list1  # it will delete the list

print('loops in list')
MyList = ['cricket', 'carrom', 'chess', 'wallyball']
print()
for i in MyList:
    print(i)
    for j in i:
        print(j)

print()
for i in range(len(MyList)):
    print(MyList[i], i)

print()
i = 0
while i < len(MyList):
    print(MyList[i], i)
    i += 1
print()

[print(x) for x in MyList]
l11 = [x for x in MyList if 'a' in x]
print(l11)
l22 = [x.upper() for x in MyList]
print(l22)

print('sort list')
MyList.sort()
print(MyList)

l1 = [21, 212, 2121, 2121, 222, 32, 3, 32]
l1.sort()
print(l1)

print('revers list')
MyList.sort(reverse=True)
print(MyList)
l1.sort(reverse=True)
print(l1)
l1.reverse()
print(l1)

print('copy list')
newl1 = l1.copy()
print(MyList)
newl2 = list(l1)
print(newl2)
newl3 = []
newl3.extend(MyList)
print(newl3)

print('add one list in another with + .')
LIS = MyList + l1
print(LIS)

print(LIS.count(3))

la = ['b', 'i', 'r', 'e', 'n']
lq = ['r', 'i', 'k', 'e', 'n']
print(set(la) - set(lq))

print('yes' in LIS)

l1 = [21, 212, 2121, 2121, 222, 32]
l2 = [21, 212, 2121, 2121, 222]
for i in range(len(l1)):
    if i < len(l2):
        print(l1[i] - l2[i], end=',')
print()

idx = 3
l2 = l2[idx:] + l2[:idx]
for i in range(len(l1)):
    if i < len(l2):
        l1[i] += l2[i]
print(l1)

l1 = [2, 5, 7]
l2 = [3, 4]
for i in range(1, 1001):
    flag = 0
    for j in l1:
        if i % j == 0:
            flag += 1
    if flag == len(l1):
        for j in l2:
            if i % j != 0:
                flag += 1
    if flag == (len(l2) + len(l1)):
        print(i)

l1 = [2, 5, 7]
l2 = [3, 4]
[print(rec) if all(rec % div == 0 for div in l1) and not any(rec % non_div == 0 for non_div in l2) else '' for rec in
 range(1, 1000)]

# result = []
# for i in range(1, 1001):
#     if i == 1:
#         continue
#     count = 0
#     for j in l1: count += 1 if i % j == 0 else 0
#     for j in l2: count += 1 if i % j != 0 else 0
#     if count == (len(l1) + len(l2)):
#         result.append(i)
# print(result)

i = 70
print('Num',i.__divmod__(3),'Reminder')
