import pandas as pd

mylist1 = [{'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
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


x={}
for i in range(0,len(mylist1)):
    if mylist1[i]['warehouse'] not in x:
        x.update({mylist1[i]['warehouse']:[]})
        x[mylist1[i]['warehouse']].insert(i,{"product":mylist1[i]['product'],"quantity":mylist1[i]['quantity']})
    else:
        x[mylist1[i]['warehouse']].insert(i,{"product":mylist1[i]['product'],"quantity":mylist1[i]['quantity']})


output={}
for i in mylist1:
    wh=i.get('warehouse')
    if wh not in output:
        output.update({wh:[]})
    output.get(wh).append({"product":i.get('product'),"quantity":i.get('quantity')})

print(output)

# a=[]
# a=output.keys()

