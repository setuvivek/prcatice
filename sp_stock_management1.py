import pandas as pd


class customer:
    data=[]
    customer_id=[1]
    cust_pan=[]
    def input(self):
        self.name=''
        self.type=''
        self.pan=''
        id = self.customer_id[-1]
        cust_type = {"1": "Customer", "2": "Vendor", "3": "Cust&Vend"}
        while True:
            print("Customer Id : {}".format(id))
            self.name = input("Enter Customer Name : ").lower()
            type_in=input("1 : Customer\t2 : Vendor\t3 : Cust/Vend\nenter digit for Customer type :").lower()
            self.type=cust_type.get(type_in)
            while True:
                self.panin = input("Enter Customer Pan : ").lower()
                if self.panin not in self.cust_pan:
                    self.cust_pan.append(self.panin)
                    self.pan = self.panin
                    break
                else:
                    print("pan already exists..try again")
            self.temp={"id":id,"name":self.name,"type":self.type,"pan":self.pan}
            self.data.append(self.temp)
            id+=1
            self.customer_id.append(id)
            self.ans = input("again ? y/n: ")
            if self.ans.lower() == "n":
                break

    def print(self):
        self.df = pd.DataFrame(self.data)
        self.df.to_csv()
        print(self.df)


class product:
    prod=[]
    prod_id = [1]
    def input(self):
        id=self.prod_id[-1]
        self.name_prod = ""
        self.in_prod = 0
        self.out_prod = 0
        self.prod_name = []
        while True:
            print("Product Id : {}".format(id))
            while True:
                self.name = input("Enter Prod. name : ").lower()
                if self.name not in self.prod_name:
                    self.prod_name.append(self.name)
                    self.name_prod = self.name
                    break
                else:
                    print("prod already exists..try again")
            self.in_prod = int(input("Enter Incoming qua : "))
            while True:
                self.out_prod = int(input("Enter Outgoing qua : "))
                if self.out_prod <= self.in_prod:
                    break
                else:
                    print("prod outgoing cant greater than incoming")
            self.onhand=self.in_prod-self.out_prod
            self.temp = {"id":id, "name": self.name_prod, "incoming": self.in_prod,
                    "outgoing": self.out_prod, "onhand": self.onhand}

            self.prod.append(self.temp)
            self.prod_id.append(id)
            id+=1
            self.prod_id.append(id)
            self.ans = input("again ? y/n: ")
            if self.ans.lower() == "n":
                break

    def income(self,id,qua):
        self.id = id
        self.qua = qua
        self.prod[id-1]['incoming']+=self.qua
        self.prod[id - 1]['onhand'] += self.qua

    def outgo(self,id,qua):
        self.id=id
        self.qua=qua
        if self.prod[id - 1]['onhand'] >= self.qua:
            self.prod[id - 1]['outgoing'] += self.qua
            # self.prod[id - 1]['incoming'] -= self.qua
            self.prod[id - 1]['onhand'] -= self.qua
            self.flag = True

    def print(self):
        self.df = pd.DataFrame(self.prod)
        self.df.to_csv()
        print(self.df)


class stock(customer,product):
    stock_data=[]
    stock_id=[1]
    def input(self):
        id=self.stock_id[-1]
        self.cust_id=''
        self.product_id=''
        self.quantity=0
        self.type=0
        option_stock_type = {"1": 'incoming', "2": 'outgoing'}
        while True:
            print("Stock Id : {}".format(id))
            while True:
                self.cust_id = int(input("Enter Customer ID : "))
                if self.cust_id in super().customer_id and super().data[0]:
                    break
                elif self.cust_id not in super().customer_id:
                    print("Customer ID Not Found..Try again")
            while True:
                self.product_id = int(input("Enter Product ID : "))
                if self.product_id in super().prod_id and super().prod[0]:
                    break
                else:
                    print("Product ID Not Found..Try again")

            while True:
                self.inputstock_type = input("1 : Incoming\t2 : Outgoing\nEnter digit for Stock type :").lower()
                if self.inputstock_type == '1' or self.inputstock_type == '2':
                    self.type = option_stock_type.get(self.inputstock_type)
                    if self.type == 'incoming':
                        self.quantity = int(input("Enter Quantity : "))
                        super().income(self.product_id, self.quantity)
                        break
                    elif self.type == 'outgoing':
                        while True:
                            self.quantity = int(input("Enter Quantity : "))
                            if super().prod[self.product_id-1]['onhand'] >=self.quantity:
                                super().outgo(self.product_id, self.quantity)
                                break
                            else:
                                print("Not enough stock , stock : ", self.prod[self.product_id - 1]['onhand'])
                    break
                else:
                    print("Enter valid Input either 1 or 2\n")

            if self.quantity!=0:
                self.temp = {"id": id,"Customer ID":self.cust_id, "Product id": self.product_id, "Quantity": self.quantity, "Stock Type": self.type}
                self.stock_data.append(self.temp)
            else:print("No Stock updated ")

            id += 1
            self.stock_id.append(id)
            self.ans = input("again ? y/n: ")
            if self.ans.lower() == "n":                break

    def print(self):
        self.df = pd.DataFrame(self.stock_data)
        self.df.to_csv()
        print(self.df)


while True:
    action=input("1 : Customer Table\t2 : Product Table\t3 : Stock Table\t\t4 : Show Tables\t\texit\nEnter digit to Select : ").lower()
    try:
        if action!='exit':
            if action=='1':
                customer().input()
            elif action=='2':
                product().input()
            elif action=='3':
                stock().input()
            elif action=='4':
                show=input("1 : Customer Table\t2 : Product Table\t3 : Stock Table\t all : 'all' :").lower()
                if show=='1':
                    customer().print()
                elif show == '2':
                    product().print()
                elif show == '3':
                    stock().print()
                elif show == 'all':
                    customer().print()
                    product().print()
                    stock().print()
        elif action=='exit':
            break
    except:
        print("Enter Valid Input")


# customer().input()
# product().input()
# stock().input()
# customer().print()
# product().print()
# stock().print()


