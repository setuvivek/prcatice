#Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
#Output : 2
count = 0
list4 = ['abc', 'xyz', 'aba', '1221']
for i in list4:
    if len(i) >= 2 and i[0] == i[-1]:
        count+=1
print(count)



#count the unique value in the list
# list20 = [1,2,3,4,5,6,7,3,52,2,4,4,2]
# l2 = []
# count = 0
# for i in list20:
#     if i not in l2:
#         count+=1
#         l2.append(i)
# print(count)