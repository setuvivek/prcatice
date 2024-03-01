list1 = [1,5,2,7,9]
list2 = [0,-2,3,1]
# output = [1,3,5,8,9]



for i in list1:
    index = list1.index(i)
    if index < len(list2):
        list1[index] = list1[index] + list2[index]
print(list1)


# list = []
# # l1 = len(list1)
# # l2 = len(list2)
# # length = max(l1,l2)
# for i in range(length):
#     a = list1[i] if i < l1 else 0  #index < length = subtraction otherwise 0
#     b = list2[i] if i < l2 else 0
#     list.append(a-b)
# print(list)
#











