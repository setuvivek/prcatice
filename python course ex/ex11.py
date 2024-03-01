a = [{'product': 'abc', 'qty': 20}, {'product': 'xyz', 'qty': 10}, {'product': 'gds', 'qty': 30},
     {'product': 'def', 'qty': 100}]


def myfunc(product_name):
    filtered_products = list(filter(lambda x: x['product'] == product_name, a))
    if filtered_products:
        sorted_products = sorted(filtered_products, key=lambda x: x['qty'])
        print(sorted_products)
    else:
        print("Product not found")


product_name = input("Enter product name: ")
myfunc(product_name)
