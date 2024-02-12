dict = [
    {'quantity': 20, 'warehouse': 'san francisco'},
    {'quantity': 40, 'warehouse': 'san francisco'},
    {'quantity': 50, 'warehouse': 'san francisco'},]
def process_document(dict):
    for index, i in enumerate(dict):   #Allow loop for contineous iterations
        qty = i['quantity']
        warehouse = i['warehouse']

        if index % 2 == 0:
            new_qty = qty * 100
            new_warehouse = f'even_{warehouse}'
        else:
            new_qty = qty - 100
            new_warehouse = f'odd_{warehouse}'
        i['quantity'] = new_qty
        i['warehouse'] = new_warehouse

    return dict

process1_document = process_document(dict)

for item in process1_document:
    print(item)




#list = [{"quantity":12,"warehouse":"france"},
#         {"quantity":5,"warehouse":"france"}]
#
#     for i in list:
#         qty = i["quantity"]
#         warehouse = i["warehouse"]
#         if i % 2 == 0:
#             new_quantity = qty * 1000
#             new_warehouse = even{warehouse}
#
#         else:
#             new_quantity = qty - 100
#             new_warehouse = odd{warehouse}
#
#         itam["quantity"] = new_quantity
#         item["warehouse"] = new_warehouse
#
#     print(item)
#