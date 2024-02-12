a = [{'product': 'abc', 'qty': '20'},
     {'product': 'xyz', 'qty': '10'},
     {'product': 'gds', 'qty': '30'},
     {'product': 'efg', 'qty': ' 100'}]
p1 = input("enter product")
final = list(filter(lambda x: x['product'] == p1, a))
if final:
    # sort_final = sorted(final, key=lambda x: x['qty'])
    sort_product = sorted(a, key=lambda x: x['product'])
    print("Product sorting",sort_product)
    sort_qty = sorted(a, key=lambda x: x['qty']) #- it generate sometimes key error=you can use "dict.get" to suppress KeyError supplying a "default value of 0:" u
    #use insted of-sort_qty = sorted(a, key=lambda x: int(x.get('qty',0)))
    # print("sort final", sort_final)
    print("Qty sorting", sort_qty)
else:
    print("product not found")


