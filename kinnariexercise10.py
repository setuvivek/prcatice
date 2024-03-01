a =[{'product':'abc','qty':20},{'product': 'xyz' , 'qty' : 10},{'product' : 'gds' , 'qty' : 30},{'product' : 'def' , 'qty': 100}]
b = input("Enter Product: ")


final = list(filter(lambda x:x['product']==b , a ))
if final:
    print(final)
else:
    print("product not found")
# list = []
# for i in a:
#     if i['product'] == b:
#         list.append(i)
#         print(list)

#
# final = list(filter(lambda i: print(i) if i['product']==b  else print("product not found"), a))
# print(final)
#
# raise Exception('There has been an error in the system')
# def fun():
#     for i in a:
#         if i['product'] == b:
#             print(i)
#             break;
#         else:
#             print("product not found")
#             break;
#
# result = filter(fun() , b)
# print(result)


