'''
[1] Output: 

{‘san francisco’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ } , 
                    { ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ }] ,
‘Chicago’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ } , 
             { ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘16.0’ }]}

[2] Output:

 {‘san francisco’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘32’ }],
‘Chicago’ : [{ ‘product’ : ‘'furn_0789’,‘Quantity’ : ‘32’ }]}


[3] In given document check whether index is even / odd if index 
Even⇒qty * 100 and edit the warehouse as : ‘even_san francisco’ .
Odd => qty - 100 and edit  the warehouse as : ‘odd_san francisco’.

'''

mylist1 = [
        {'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
        {'product': 'furn_6666', 'quantity': 16.0, 'warehouse': 'san francisco'},
          {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'san francisco'},
          {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'san francisco'},
          {'product': 'e-com10', 'quantity': 22.0, 'warehouse': 'san francisco'},
          {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'san francisco'},
          {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'san francisco'},
          {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'san francisco'},
          {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'san francisco'},
          {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'san francisco'},
          {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'san francisco'},
          {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'san francisco'},
          {'product': 'furn_0269', 'quantity': 10.0, 'warehouse': 'san francisco'},
          {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'san francisco'},
          {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'san francisco'},
          {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'san francisco'},
          {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
          {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
          {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7888', 'quantity': 125.0, 'warehouse': 'san francisco'},
          {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'san francisco'},
          {'product': 'furn_0789', 'quantity': 60.0, 'warehouse': 'chicago'},
          {'product': 'furn_6666', 'quantity': 60.0, 'warehouse': 'chicago'},
          {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'chicago'},
          {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'chicago'},
          {'product': 'e-com18', 'quantity': 22.0, 'warehouse': 'chicago'},
          {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'chicago'},
          {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'chicago'},
          {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'chicago'},
          {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'chicago'},
          {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'chicago'},
          {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'chicago'},
          {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'chicago'},
          {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'chicago'},
          {'product': 'furn_0269', 'quantity': 18.0, 'warehouse': 'chicago'},
          {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'chicago'},
          {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'chicago'},
          {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'chicago'},
          {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'chicago'},
          {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'chicago'},
          {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'chicago'},
          {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'chicago'},
          {'product': 'furn_7888', 'quantity': 150.0, 'warehouse': 'chicago'},
          {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'chicago'},
          {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'chicago'},
          {'product': 'e-com18', 'quantity': 25.0, 'warehouse': 'chicago'},
          {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'chicago'},
          {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'san francisco'},
          {'product': 'e-com10', 'quantity': 25.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7888', 'quantity': 75.0, 'warehouse': 'san francisco'},
          {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
          {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
          {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
          {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
          {'product': 'furn_6666', 'quantity': 10.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7777', 'quantity': 100.0, 'warehouse': 'san francisco'},
          {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
          {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7777', 'quantity': 80.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7800', 'quantity': 16.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7800', 'quantity': 32.0, 'warehouse': 'san francisco'},
          {'product': 'e-com07', 'quantity': 50.0, 'warehouse': 'san francisco'},
          {'product': 'furn_6666', 'quantity': 20.0, 'warehouse': 'san francisco'},
          {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
          {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
          {'product': 'desk0005', 'quantity': 65.0, 'warehouse': 'san francisco'},
          {'product': 'furn_7800', 'quantity': 8.0, 'warehouse': 'san francisco'},
          {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
          {'product': 'e-com11', 'quantity': 5.0, 'warehouse': 'san francisco'},
          {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
          {'product': 'e-com11', 'quantity': 10.0, 'warehouse': 'san francisco'},
          {'product': 'desk0006', 'quantity': 70.0, 'warehouse': 'san francisco'}]


print("\t\t -- TASK-1 San Francisco list --")
# san = "san francisco"
# chg = "chicago"
for i in mylist1:
    if i["warehouse"] == 'san francisco':
        san1 = {'san francisco': {
            'product': i["product"],
            'quantity': i['quantity']
        }
        }
        print(san1)
print("\n\n")

print("\t\t -- TASK-1 Chicago list --")
for j in mylist1:
    if j["warehouse"] == 'chicago':
        chg1 = {'chicago': {
            'product': j["product"],
            'quantity': j['quantity']
        }
        }
        print(chg1)
        # print(chg1.values())
print("\n\n")


print("\t\t -- TASK-2 San Franciso list --")
san_pro_qty = {}

for i in mylist1:
    if i['warehouse'] == 'san francisco':
        product_name = i['product']
        quantity = i['quantity']
        san_pro_qty[product_name] = san_pro_qty.get(product_name, 0) + quantity

for product, quantity in san_pro_qty.items():
    print(f'Product: {product}, Quantity: {quantity}, Warehouse: san francisco')
print("\n\n")

print("\t\t -- TASK-2 Chicago list --")
chg_pro_qty = {}

for j in mylist1:
    if j['warehouse'] == 'chicago':
        product_name = j['product']
        quantity = j['quantity']
        chg_pro_qty[product_name] = chg_pro_qty.get(product_name, 0) + quantity

for product, quantity in chg_pro_qty.items():
    print(f'Product: {product}, Quantity: {quantity}, Warehouse: chicago')
print("\n\n")

chg_pro_count = {}

for j in mylist1:
    if j['warehouse'] == 'chicago':
        product_name = j['product']
        # quantity = item['quantity']
        chg_pro_count[product_name] = chg_pro_count.get(product_name, 0) + 1

for product, count in chg_pro_count.items():
    print(f'Product: {product}, Count: {count}, Warehouse: chicago')
print("\n\n")

print("\t\t -- TASK-3 San Francisco and Chicago list --")

for i, j in enumerate(mylist1):
    quantity = j['quantity']
    if i % 2 == 0:
        j['quantity'] = quantity * 100
        j['warehouse'] = f'even_{j["warehouse"]}'
    else:
        j['quantity'] = quantity - 100
        j['warehouse'] = f'odd_{j["warehouse"]}'

for j in mylist1:
    print(j)