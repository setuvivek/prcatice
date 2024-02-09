dict1 = {1: 20, 3:15 , 4:18  }
dict2 = {20:1 , 49:3 , 2:7 , 4:5}
#output = {1: 40 , 3:64 , 4:18 , 7:2 , 5:4}

for k,l in dict2.items():
    for i,j in dict1.items():
        if i == l:
            c = j+k
            dict1.update({i:c})
    dict1.update({l:k})
print(dict1)
# 2 nd way
# for a,b in dict2.items():
#     dict1.update({b:a})
# print(dict1)
# c = {**dict2,**dict1}
# print(c)

# merged_dict = dict2.copy()
#
# for key, value in dict1.items():
#     merged_dict[key] = value
#
# print(merged_dict)
# merged_bio = { **dict1, **dict2}
# print(merged_bio)
# output = {}
# for key,value in dict1.items():
#     output[key] = output.get(key,0) + value
# for key,value in dict2.items():
#     output[key] = output.get(key,0) + value
# print(output)

# for i in dict.keys():
#     for j in dict2:
#         if i == dict2[j]:
#             c = j + dict[i]
#             dict.update({i:c})
# print(dict)
# dict3 = {value : key for key,value in  dict2.items()}
# print(dict3)
# dict4 = {}
# for i in dict3:
#     if i > dict3[i]:
#         dict4.update({i : dict3[i]})
# print(dict4)
# dict.update(dict4)
# print(dict)