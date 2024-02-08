#
# [1] Write a Python program to count the occurrences of each word in a given sentence.
#
# Input: "Complete sentence Complete exercise"
#
# Output: Complete - 2
# 		sentence - 1
# 		exercise - 1

list1 = ["Complete", "sentence", "Complete", "exercise"]
s = set(list1)
# print(type(s))
for i in s:
    # flag=1
    # for j in s:
    #     if j == i:
    #      flag=0
    print(i , "-",list1.count(i))

total=0
'''
[2] Write a Python program to sum all the items in a list.

Input: [10,12,20,22]

Output: 64
'''
list2 = [10,12,20,22]
print(list2)

for i in list2:
    total+=i

print( total )

print()

'''
[3] Write a Python program to get the smallest number from a list.

Input: [10,12,20,22,2]

Output: 2
'''

list3 = [10,12,20,22,2]
list3.sort()
print(list3[0])


'''

[4] Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.	

Input : ['abc', 'xyz', 'aba', '1221']

Output : 2

'''
list4 = ['abc', 'xyz', 'aba', '1221']
nliist = []
count = 0

# nlist4=[x for x in list4 if '' in x]
# print(nlist4) ========

for i in list4:
    if '' in i:
        nliist.append(i)
print(nliist)


for j in range(len(nliist)):
    count += 1
print(count)
print()

#==--==
count=0
for i in list4:
    if i[0] == i[-1] or len(i)<=1:

        count+=1
print(count)
print()

'''

[5] Write a Python program to remove duplicate number from a list.

Input: [10,12,20,22,10]

Output: [10,12,20,22]

'''
list5=[10,12,20,22,22,10,13,14,25,25]
# [10,12,13,14,20,22,25]
nlist5=[]


# print(set(list5))


#
# v=1
#
# c=list5[v]
list5.sort()
# print(list5)
# for i in list5:
#     if i != c:
#         list5.remove(i)
#
#         v += 1
#     else:
#         print(c+5)
#         # print(i)
#
# print(list5)
for i in list5:
    for j in list5:
        if i!=j:
            print(i, end='')
        else:
            list5.remove(j)
    print()
print(list5)