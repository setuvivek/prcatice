a =[{'product':'abc','qty':20},{'product': 'xyz' , 'qty' : 10},{'product' : 'gds' , 'qty' : 30},{'product' : 'def' , 'qty': 100}]
b = input("Enter Product: ")


final = list(filter(lambda x:x['product']==b , a ))
if final:
    product_sort = sorted(a, key=lambda x: x['product'])
    print("Product sorted : " , product_sort)
    qty_sort = sorted(a, key=lambda y: y['qty'])
    print("Qty sorted : ", qty_sort)
else:
    print("product not found")
# list = []

str1 = "12345"
lis = ['1','2','3']
nums = list(map(int, input("enter : ").split()))
print(nums)


nums = [1, 2, 3]
print(*nums)
# compare = [i for i in lis[i] if str in lis]
# if compare:
#     print("ok")
# if any(str in i for i in lis):
#     print("yes")
#
# nl=list(map(str1,lis))
# print(
    # if isinstance(value, (str)):
    #     print('Input Value is String')
# final = list(filter(lambda x:x['product']==b , a ))
# if final:
#     print(final)
# else:
#     print("product not found")
# #letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# a function that returns True if letter is vowel
# def filter_vowels(letter):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return True if letter in vowels else False
#
# filtered_vowels = filter(filter_vowels, letters)
# vowels = tuple(filtered_vowels)
# print(vowels)


# def get_nam(final):
#     return final.get('product')
#     final.sort(key=get_nam)
#     print(final)

# for i in a:
#     if i['product']==b:
#         def get_name(a):
#             return a.get('product')
#         a.sort(key=get_name)
#         print(a, end='\n\n')
#
#         def get_name(a):
#             return a.get('qty')
#         a.sort(key=get_name)
#         print(a, end='\n\n')