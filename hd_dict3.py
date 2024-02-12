# dict = {}
# for i in range(2):
#     product = input("Enter product name")
#     quantity = input("Enter product quantity")
#     warehouse = input("Enter warehouse")
#     product1 = input("product")
#     quantity1 = input("quantity")
#     warehouse1 = input("warehouse")
#     dict[product] = product1
#     dict[quantity] = quantity1
#     dict[warehouse] = warehouse1
#     if warehouse in dict:
#         dict[warehouse].append({'product': product, 'Quantity': quantity})   #add related dictionary
#     else:
#
#         dict[warehouse] = [{'product': product, 'Quantity': quantity}]  #items into main dictionary
# print(dict)
dict = {}
for i in range(3):
    warehouse = input("Enter warehouse name: ")
    product = input("Enter product name: ")
    quantity = input("Enter quantity: ")
    x = {'product':product,'quantity':quantity}

    if warehouse in dict:
        dict[warehouse].append(x)
    else:
        dict[warehouse] = [x]

print(dict)

# count = 0
# while(count<3)
#     count = count + 1
#
# while True
#     x = input("another entry")
#     if x == 'no'
#         break