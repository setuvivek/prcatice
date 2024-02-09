# '''
# [1] Write a Python program to count the occurrences of each word in a given sentence.
#
# Input: "Complete sentence Complete exercise"
#
# Output: Complete - 2
#      sentence - 1
#      exercise - 1
# '''
# Input = "Complete sentence Complete exercise"
# # l1=Input.split(' ')
# print('Complete', Input.count('Complete'))
# print('sentence', Input.count('sentence'))
# print('exercise', Input.count('exercise'))
#
# '''
# [2] Write a Python program to sum all the items in a list.
#
# Input: [10,12,20,22]
#
# Output: 64
# '''
# Input = [10, 12, 20, 22]
# print(sum(Input))
# sum = 0
# for i in Input:
#     sum += i
# print(sum)
# '''
# [3] Write a Python program to get the smallest number from a list.
#
# Input: [10,12,20,22,2]
#
# Output: 2
# '''
# Input = [10, 12, 20, 22, 2]
# print(min(Input))
#
# '''
# [4] Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
#
# Input : ['abc', 'xyz', 'aba', '1221']
#
# Output : 2
# '''
# Input = ['abc', 'xyz', 'aba', '1221', 'aa', 'birenb']
# c = 0
# for i in Input:
#     if len(i) > 2 and (i[0] == i[-1]):
#         c += 1
# print(c)
# '''
# [5] Write a Python program to remove duplicate number from a list.
#
# Input: [10,12,20,22,10]
#
# Output: [10,12,20,22]
# '''
# Input = [10, 12, 20, 22, 10]
# s1 = set(Input)
# Output = list(s1)
# print(Output)
# '''
# [1] Output:
#
# {
# ‘san francisco’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ } ,
#                     { ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ }] ,
# ‘Chicago’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ } ,
#              { ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ }]
# }
# '''
# mylist1 = [{'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com10', 'quantity': 22.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0269', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7888', 'quantity': 125.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0789', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_6666', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'chicago'},
#            {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'chicago'},
#            {'product': 'e-com18', 'quantity': 22.0, 'warehouse': 'chicago'},
#            {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'chicago'},
#            {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'chicago'},
#            {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'chicago'},
#            {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0269', 'quantity': 18.0, 'warehouse': 'chicago'},
#            {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'chicago'},
#            {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'chicago'},
#            {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7888', 'quantity': 150.0, 'warehouse': 'chicago'},
#            {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'e-com18', 'quantity': 25.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com10', 'quantity': 25.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7888', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 32.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 20.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0005', 'quantity': 65.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 8.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0006', 'quantity': 70.0, 'warehouse': 'san francisco'}]
# d1 = {}
# for i in mylist1:
#     warehouse = i['warehouse']
#     d2 = {'product': i['product'], 'quantity': i['quantity']}
#     if warehouse not in d1:
#         d1[warehouse] = [d2]
#     else:
#         d1[warehouse].append(d2)
# [print(i) for i in d1.items()]
# print('1')
# '''
# [2] Output:
#
#  {‘san francisco’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘32’ }],
# ‘Chicago’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘32’ }]}
# '''
# print()
# mylist1 = [{'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com10', 'quantity': 22.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0269', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7888', 'quantity': 125.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0789', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_6666', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'chicago'},
#            {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'chicago'},
#            {'product': 'e-com18', 'quantity': 22.0, 'warehouse': 'chicago'},
#            {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'chicago'},
#            {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'chicago'},
#            {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'chicago'},
#            {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0269', 'quantity': 18.0, 'warehouse': 'chicago'},
#            {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'chicago'},
#            {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'chicago'},
#            {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7888', 'quantity': 150.0, 'warehouse': 'chicago'},
#            {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'e-com18', 'quantity': 25.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com10', 'quantity': 25.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7888', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 32.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 20.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0005', 'quantity': 65.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 8.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0006', 'quantity': 70.0, 'warehouse': 'san francisco'}
#            ]
#
# out_put = {}
# for i in mylist1:
#     warehouse = i.get('warehouse')
#     product = i.get('product')
#     quantity = i.get('quantity')
#     data = {'product': product, 'quantity': quantity}
#
#     if warehouse not in out_put:
#         out_put[warehouse] = [data]
#
#     flag = True
#     for j in out_put[warehouse]:
#         if product in j.get('product'):
#             j.get('quantity') + quantity
#             flag = False
#             break
#
#     if flag:
#         out_put[warehouse].append(data)
#
# [print(i) for i in out_put.items()]
# print('2')
# '''
# [3] In given document check whether index is even / odd if index
# Even⇒qty * 100 and edit the warehouse as : ‘even_san francisco’ .
# Odd => qty - 100 and edit  the warehouse as : ‘odd_san francisco’.
# '''
# mylist1 = [{'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com10', 'quantity': 22.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0269', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7888', 'quantity': 125.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_0789', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_6666', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'chicago'},
#            {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'chicago'},
#            {'product': 'e-com18', 'quantity': 22.0, 'warehouse': 'chicago'},
#            {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'chicago'},
#            {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'chicago'},
#            {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'chicago'},
#            {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'chicago'},
#            {'product': 'furn_0269', 'quantity': 18.0, 'warehouse': 'chicago'},
#            {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'chicago'},
#            {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'chicago'},
#            {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7888', 'quantity': 150.0, 'warehouse': 'chicago'},
#            {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'chicago'},
#            {'product': 'e-com18', 'quantity': 25.0, 'warehouse': 'chicago'},
#            {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'chicago'},
#            {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com10', 'quantity': 25.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7888', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7777', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 16.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 32.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 50.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 20.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0005', 'quantity': 65.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_7800', 'quantity': 8.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
#            {'product': 'e-com11', 'quantity': 10.0, 'warehouse': 'san francisco'},
#            {'product': 'desk0006', 'quantity': 70.0, 'warehouse': 'san francisco'}]
# print()
# for i in range(len(mylist1)):
#     if i % 2 == 0:
#         mylist1[i]['quantity'] *= 100
#     if i % 2 != 0:
#         mylist1[i]['quantity'] -= 100
#
# for i in mylist1:
#     print(i)
# print('3')
