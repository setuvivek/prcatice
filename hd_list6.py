list10 = [1,2,3,4,5,6]
even_count = 0
odd_count = 0
for i in list10:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count, odd_count)



# remove even element in the list
# list11 = [1,2,3,4,5,6,7,8]
# for i in list11:
#     if i % 2 == 0:
#         list11.remove(i)
# print(list11)




# -print duplicate from the list
# list12 = [1,2,3,4,5,6,2,3,4,5]
# unique = []
# duplicate = []
# for i in list12:
#     if i not in unique:
#         unique.append(i)
#     elif i not in duplicate:
#         duplicate.append(i)
# print(duplicate)