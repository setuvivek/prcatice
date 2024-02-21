class Customer:

    customer_list = []

    def __init__(self, id, name, type, pan):
        self.id = id
        self.name = name
        self.type = type
        self.pan = pan

    @classmethod
    def add_customer(cls,customer):
        for i in cls.customer_list:
            if i.id == customer.id:
                print(" customer id must be unique")
                return

        if customer.type not in {'customer', 'vendor', 'customer,vendor'}:
            print("enter valid type of customer")
            return

        for j in cls.customer_list:
            if j.pan == customer.pan:
                print("customer pan must be unique")
                return

        cls.customer_list.append(customer)

    @classmethod
    def print_customer(cls):
        print("customer record")
        for k in cls.customer_list:
            print(f"Customer id:{k.id}, Customer name: {k.name}, Customer type: {k.type}, Customer pan: {k.pan}")


class Product:
    product_list = []

    def __init__(self, _id, name, incoming, outgoing):
        self.id = _id
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
        self.onhand = self.incoming - self.outgoing

    @classmethod
    def add_product(cls,product):
        for x in cls.product_list:
            if x.id == product.id:
                print("product id must be unique")
                return

        for y in cls.product_list:
            if y.name == product.name:
                print("product name must be unique")
                return

        if product.incoming < product.outgoing:
            print("stock is not available")
            return

        if product.onhand < 0:
            print("onhand is not negative")
            return

        cls.product_list.append(product)

    @classmethod
    def print_product(cls):
        print("product record")
        for z in cls.product_list:
            print(f"Product id:{z.id},Product name: {z.name}, Incoming product: {z.incoming}, outgoing Product: {z.outgoing}, Onhand :{z.onhand}")

class Stock(Customer, Product):
    stock_list = []

    def __init__(self, id, customer_id, product_id, qty, type):
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.qty = qty
        self.type = type

    @classmethod
    def add_stock(cls,stock):
        # cls.stock_list.append(stock)

        for k in cls.stock_list:
            if k.id == stock.id:
                print("stock id must be unique")
                return

        if stock.type not in {'incoming','outgoing'}:
            print("enter valid product type")
            return

        for product in cls.product_list:
            if product.id == stock.product_id:
                if stock.type == 'incoming':
                    product.incoming += stock.qty
                    product.onhand += stock.qty

                elif stock.type == 'outgoing':
                    if product.onhand >= stock.qty:
                        product.outgoing += stock.qty
                        product.onhand -= stock.qty
                    else:
                        print("outgoing does not exists stock quantity")
                        return False
        product.onhand = product.incoming - product.outgoing

        cls.stock_list.append(stock)


    @classmethod
    def print_stock(cls):
        print("stock record")
        for l in cls.stock_list:
            print(f"stock id:{l.id}, Customer id:{l.customer_id}," f"Product id: {l.product_id}, Product qty:{l.qty}, Product type:{l.type}")


def fun(prompt):
    while True:
        i = input(prompt)
        if i.strip():
            return i

def fun1(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("enter valid number")

while True:
    class_name = input("enter class name to add data(customer,product,stock) or write 'exit' to stop ")

    if class_name == 'exit':
        break

    if class_name == 'customer':
        id = fun("enter customer id")
        name = fun("enter customer name")
        type = fun("enter customer type('customer','vendor','customer,vendor')")
        pan = fun("enter customer pan")

        new_customer = Customer(id, name, type, pan)
        Customer.add_customer(new_customer)



    elif class_name == 'product':
        id = fun("enter product id")
        name = fun("enter product name")
        incoming = fun1("enter incoming product")
        outgoing = fun1("enter outgoing product")

        new_product = Product(id, name, incoming, outgoing)
        Product.add_product(new_product)


    elif class_name == 'stock':
        id = fun("enter stock id")
        customer_id = fun("enter customer id")
        product_id = fun("enter product id")
        qty = fun1("enter product qty")
        type = fun("enter product type(incoming, outgoing)")

        new_stock = Stock(id, customer_id, product_id, qty, type)
        Stock.add_stock(new_stock)

Customer.print_customer()
Product.print_product()
Stock.print_stock()

