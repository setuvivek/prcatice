class salesorder:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.lines = []

    def add(self):
        self.name = input("Enter a name")
        self.email = input("Enter an email")

        for i in range(3):
            product = input("Enter product")
            qty = input("Enter quantity")
            price = input("Enter price")
            lines: dict[str, str] = {'product': product, 'qty': qty, 'price': price}
            self.lines.append(lines)

    def print(self):
        data = {'name': self.name, 'email': self.email, 'lines': self.lines}
        print(data)


if __name__ == "__main__":
    obj = salesorder()
    obj.add()
    obj.print()
