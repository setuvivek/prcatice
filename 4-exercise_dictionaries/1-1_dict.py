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
    {'product': 'e-com11', 'quantity': 10.0, 'warehouse': 'India'},
    {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'India'},
    {'product': 'desk0006', 'quantity': 70.0, 'warehouse': 'san francisc'}]


print("\t\t -- TASK-1 San Francisco list --")

data = {}
for i in mylist1:
    ware = i['warehouse']
    element = {'product': i['product'], 'quantity': i['quantity']}
    lst = []
    data.setdefault(ware, lst).append(element)

# SIR CODE
# data = {}
# for i in mylist1:
#     warehouse = i.get('warehouse')
#     product = i.get('product')
#     quantity = i.get('quantity')
#     if not data.get(warehouse):
#         data.update({warehouse: []})
#     data.get(warehouse).append({'product': product, 'quantity': quantity})
# print(data)


# for key, value in data.items():
#     print("\n", key, "\n", value)
#     print(type(data))
