class Order:
    name = str(),
    email = str(),
    product = str(),
    qty = int(),
    cost = float()

    def set_data(self):

        if len(name) > 0:
            self.name = name
        if len(email) > 0:
            self.email = email
        if len(product) > 0:
            self.product = product
        if qty > 0:
            self.qty = qty
        if cost > 0:
            self.cost = cost

    def get_data(self):
        return (f"Customer: {self.name}\nEmail: {self.email}\nProduct: {self.product}"
                f"\nQuantity: {self.qty}\nCost per Unit: ${self.cost:.2f}\n")


name = input("Enter customer name: ")
email = input("Enter customer email: ")
product = input("Enter product name: ")
qty = int(input("Enter quantity: "))
cost = float(input("Enter cost per unit: "))


order = Order()
order.set_data()

order2 = Order()
order2.set_data()

order3 = Order()
order3.set_data()

order4 = Order()
order4.set_data()

order5 = Order()
order5.set_data()

if order or order2 or order3 or order4 or order5:
    print(order.get_data())
