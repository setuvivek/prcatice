list1 = [5,7,9,3]
list2 = [3,6,4]

a = int(input("Enter index : "))
d = len(list2)
new_list = list2[:]+list2[:a]
#print(new_list)
j = 0
for i in range(a,len(new_list)):
    if j < len(list1):
        list1[j] = list1[j] + new_list[i]
        j += 1
    i += 1
print(list1)


# a = int(input("Enter index : "))
# list = []
# for i in range(a, len(list2)):
#     list.append(list2[i])
# print(list)
# def move_element(input_list, index_old, index_new):
#     if index_old < 0 or index_old > len(input_list) - 1:
#         print("Index doesn't exist.")
#     else:
#         tmp = input_list[index_old]
#         input_list[index_old] = input_list[index_new]
#         input_list[index_new] = tmp
# list2 = [3,6,4]

# using lambda to print table of 10
# numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
#
# print(numbers)
# words = ["apple", "banana", "cherry", "orange"]
# word_lengths = [len(word) for word in words]
# print(word_lengths)


# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of students: ", x)
# input list
# lst = [10, 11, 12, 13, 14, 15]
# # the above input can also be given as
# # lst=list(map(int,input().split()))
# l = []  # empty list
#
# # iterate to reverse the list
# for i in lst:
#     # reversing the list
#     l.insert(0, i)
# # printing result
# print(l)


# list2 = [3,6,4]
# current_index = 1
# new_index = 2
# element = list2.pop(current_index)
# list2.insert(new_index, element)
# print(list2)
# move_element(list2, 1, a)
# print(list2)  # [A,C,B]
# j = 0
# for i in range(0, len(list2)):
#     if j < len(list1):
#         list1[j] = list1[j] + list2[i]
#         j += 1
#     i += 1
# print(list1)
#
# lists = list(map(lambda x: x.replace(0, a), list2))
# print(lists)
# a = int(input("Enter index : "))
# index = list2.index(a)
# list2 = list2[:index]+ list2[index+1:]
# print(list2)
#     d = len(list2)
#     a = int(input("Enter index : "))
#     j = 0
#     if a <= d:
#         if j < len(list1):
#             list1[j] = list1[j] + list2[a]
#             j += 1
# print(list1)
#
#
# fun(list1,list2)
# i = 0
# n = 10
#
# while i < n:
#     if i < 5:
#         print(i)
#         i += 1
#     else:
#         i = 0  # This assignment restarts the loop

# # i    l = 1
#        l = 1
#     if i == len(list2)-1:
#         for k in range(0, len(list2)):
#             if l < len(list1):
#                 list1[l] = list1[l] + list2[k]
#                 l += 1
#             k += 1
#
#
#  if i == len(list2)-1:
#         for k in range(0, len(list2)):
#             if l < len(list1):
#                 list1[l] = list1[l] + list2[k]
#                 l += 1
#             k += 1
#
#
# f a == len(list2)-1:
#   for i in range(a, len(list2), -2):
#         print(list[a])
#
# j = 1
# if j < len(list1):
#     for a in  range(len(list2)):
#         if a == len(list2)-1:
#             a=0
#             print(list2[a])
#             list1[j] += list2[a]
#         a+=1
# j += 1
# print(list1)
# for i in range(a, len(list2)):
#     for j in range(len(list1)):
#         list1[j] = list1[j] +  list2[i]
#         j += 1
#
# print(list1)

# for i in list2:
#     for j in list1:
#         #list1[j] = list1[j] + list2[i]
#         j = j + i
#         # print(list1)
#         #i += 1

#print(list1)

#
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         list1[i] = list1[i] + list2[j]
#         break
# print(list1)
# i = 0
# while i < len(list2):
#     for j in range(len(list1)):
#         list1[j] = list1[j] + list2[i]
#         i += 1
# print(list1)

