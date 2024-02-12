a = [{'product': 'abc', 'qty': '20'},
     {'product': 'xyz', 'qty': '10'},
     {'product': 'gds', ' qty': '30'},
     {'product': 'efg', 'qty': ' 100'}]
p1 = input("enter product")

final = list(filter(lambda x: x['product'] == p1, a))
if final:
    print(final)
else:
    print("product not found")
