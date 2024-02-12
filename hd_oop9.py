from typing import Dict

class salesorder:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.lines = []
    def set(self):   #call method m1 5 times
        self.name = input("Enter a name")
        self.email = input("Enter an email")

        for i in range(2):
            product = input("Enter a product")
            qty = input("Enter a qty")
            price = input("Enter price")
            lines: dict[str, str] = {'product': product, 'qty': qty, 'price': price}
            self.lines.append(lines)

    def get(self):  #call method m2 only one time
        data: dict[str, str] = {'name':self.name,'email':self.email,'lines':self.lines}
        return data

if __name__ == "__main__":
    order = []
    for j in range(5):
        obj = salesorder()
        obj.set()
        # obj.m2()
        order.append(obj)

    print(order[0].get())
