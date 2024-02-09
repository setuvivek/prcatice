# 1] Write a Python program to count the occurrences of each word in a given sentence.
# Input: "Complete sentence Complete exercise"
# Output: Complete - 2
# 		sentence - 1
# 		exercise - 1
l = "Complete sentence Complete exercise"
print(l.count('Complete'))
print(l.count('sentence'))
print(l.count('exercise'))


# 2] Write a Python program to sum all the items in a list.
# Input: [10,12,20,22]
# Output: 64
num = [10,12,20,22]
x = sum(num)
print(x)


# [3] Write a Python program to get the smallest number from a list.
# Input: [10,12,20,22,2]
# Output: 2

list1 = [10,12,20,22,2]
x = list1.sort()
print(list1[0])


#[4] Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
#Input : ['abc', 'xyz', 'aba', '1221']
#Output : 2
list1 = ['abc', 'xyz', 'aba', '1221']
c = 0
for i in list1:
    if i[0]==i[-1]:
        c +=1
print(c)




# #[5]Write a Python program to remove duplicate number from a list.
# #Input: [10,12,20,22,10]
# #Output: [10,12,20,22]
#
list1 = [10,12,20,22,10]
x = set(list1)
y = list(x)
print(y)

