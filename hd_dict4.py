data = {}
def add_product():
    if warehouse in data:
        warehouse_data = data[warehouse] #store data based on warehouse
        # product_exists = False
        for i in warehouse_data:
            if i['product'] == product:
                i['Quantity'] += qty   #product exist add quantity
                # product_exists = True
                break
        # if not product_exists:
        #     warehouse_data.append({'product': product, 'Quantity': qty})
    else:

        data[warehouse] = [{'product': product, 'Quantity': qty}]

for i in range(4):
    warehouse = input("Enter warehouse name : ")
    # if warehouse == 'exit':-using while loop
    #     break
    product = input("Enter product name: ")
    qty = float(input("Enter quantity: "))

    add_product() #to add new entry from user

print(data)


# print("data:",data)
        #    keysum = 0
        #    for k in data:
        #       keysum += k
        #       print("sum of quantity",keysum)