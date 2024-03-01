a = [{'product': 'abc', 'qty': 20}, {'product': 'xyz', 'qty': 10}, {'product': 'gds', 'qty': 30},
     {'product': 'def', 'qty': 100}]


def find_product(product_name):
    filtered_products = list(filter(lambda x: x['product'] == product_name, a))
    if filtered_products:
        print(filtered_products[0])
    else:
        print("Product not found")


user_product = input("Enter product name: ")

find_product(user_product)
