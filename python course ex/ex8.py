'''
class sales_order:
    sales_info = {}
    cust_name = str()
    email = str()
    product = str()
    qty = int()
    cost = int()

    def sales_data(self):
        self.cust_name = input('enter your name : ')
        self.email = input('enter your email : ')
        self.product = input('enter your product : ')
        self.qty = int(input('enter qty :'))
        self.cost = int(input('enter cost :'))

    def print_data(self):
        self.sales_info = {'cust_name': self.cust_name, 'email ': self.email, 'product': self.product, 'qty': self.qty,
                           'cost': self.cost}
        print(self.sales_info)


s1 = sales_order()
s1.sales_data()
s1.print_data()
'''


class SalesOrder:
    name = str()
    email = str()
    lines = []
    product = str()
    qty = int()
    price = float()

    def get_order_details(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.product = input("Enter product name : ")
        self.qty = int(input("Enter quantity: "))
        self.price = float(input("Enter price per item: "))

        self.lines.append({'Product': self.product, 'qty': self.qty, 'price': self.price})

    def print_order_details(self):
        order_dict = {'Name': self.name, 'Email': self.email, 'lines': self.lines}
        print(order_dict)


order = SalesOrder()
order.get_order_details()
order.print_order_details()
