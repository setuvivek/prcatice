class add:
    first_number = 0
    second_number = 0
    third_number = 0

    def __init__(self, f, s):
        self.first_number = f
        self.second_number = s

    def m3(self):
        print("first number" + str(
            self.first_number))
        print("second number" + str(self.second_number))
        print("addition of two numbers" + str(self.third_number))

    def calculate(self):
        self.third_number = self.first_number + self.second_number


obj3 = add(10, 20)
obj3.calculate()
obj3.m3()