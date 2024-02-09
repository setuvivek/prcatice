import itertools


class Customer_Master:
    Customer_Detail = {}
    CUST_ID = itertools.count(1)
    CUST_NAME = str()
    CUST_TYPE = []
    CUST_PAN = str()

    def CUST_Data_Get(self):
        while True:
            print('Customer Details')
            choice = int(input(
                "1.insert data\n2.print data\n3.delete data of id no\n11.ENTER 11 TO EXIT\nCHOSE YOUR OPERATION :- "))
            print()
            if choice == 1:
                cust_id_count = next(self.CUST_ID)
                print("CUSTOMER ID :- ", cust_id_count)
                self.CUST_NAME = input("CUSTOMER NAME :- ")
                if self.CUST_NAME == '':
                    print("NAME CAN'T BLANK\n")
                    return Customer_Master().CUST_Data_Get()
                print("1.customer\n2.vendor\n3.customer,vendor\nCHOSE YOUR OPERATION :- ")
                TYPE = int(input("CUSTOMER TYPE *(customer, vendor) :- "))
                if TYPE == 1:
                    self.CUST_TYPE = ["customer"]
                elif TYPE == 2:
                    self.CUST_TYPE = ["vendor"]
                elif TYPE == 3:
                    self.CUST_TYPE = ["customer", "vendor"]
                else:
                    print("ENTER VALID OPTION.\n")
                    return Customer_Master().CUST_Data_Get()
                self.CUST_PAN = input("CUSTOMER PAN :- ")
                if self.CUST_PAN == '':
                    print("PAN NO. CAN'T BLANK\n")
                    return Customer_Master().CUST_Data_Get()
                print()
                for i in range(1, len(self.Customer_Detail) + 1):
                    if self.CUST_PAN == self.Customer_Detail[i].get("CUST_PAN"):
                        print("ID ALREADY EXISTS\n")
                        print(self.Customer_Detail[i])
                        return Customer_Master().CUST_Data_Get()
                self.Customer_Detail[cust_id_count] = {cust_id_count: cust_id_count, "CUST_NAME": self.CUST_NAME,
                                                       "CUST_TYPE": self.CUST_TYPE, "CUST_PAN": self.CUST_PAN}
            elif choice == 2:
                print(self.Customer_Detail)
                return Customer_Master().CUST_Data_Get()
            elif choice == 3:
                ID = int(input("ENTER ID :- "))
                if ID not in self.Customer_Detail.keys():
                    print("ENTER VALID ID.\n")
                    return Customer_Master().CUST_Data_Get()
                self.Customer_Detail.pop(ID)
            elif choice == 11:
                break
            else:
                print("Enter valid option")


class Product_Master(Customer_Master):
    Product_Detail = {}
    PROD_ID = itertools.count(1)
    PROD_NAME = str()
    PROD_INCOMING = 0.0
    PROD_OUT_GOING = 0.0
    PROD_STOCK = 0.0

    def PRODU_GET_DATA(self):
        while True:
            print('Product Master')
            choice = int(input(
                "1.insert data\n2.print data\n11.ENTER 11 TO EXIT\nCHOSE YOUR OPERATION :- "))
            print()
            if choice == 1:
                prod_id_count = next(self.PROD_ID)
                print("PRODUCT ID :- ", prod_id_count)
                self.PROD_NAME = input("PRODUCT NAME :- ")
                if self.PROD_NAME == '':
                    print("NAME CAN'T BLANK\n")
                    return Product_Master().PRODU_GET_DATA()
                for name in range(1, len(self.Product_Detail) + 1):
                    if self.PROD_NAME == self.Product_Detail[name].get('PROD_NAME'):
                        print("NAME ALREADY EXISTS")
                        print(self.Product_Detail[name].get('PROD_NAME'))
                        return Product_Master().PRODU_GET_DATA()
                self.Product_Detail[prod_id_count] = {"PROD_ID": prod_id_count,
                                                      "PROD_NAME": self.PROD_NAME, "PROD_INCOMING": 0.0,
                                                      "PROD_OUT_GOING": 0.0,
                                                      "PROD_STOCK": 0.0}
            elif choice == 2:
                print(self.Product_Detail)
                return Product_Master().PRODU_GET_DATA()
            elif choice == 11:
                break
            else:
                print("Enter valid option")


class Stock_Master(Product_Master, Customer_Master):
    Stock_Detail = {}
    STOCK_ID = itertools.count(1)
    PROD_ID = 0
    CUST_ID = 0
    STOCK_QUANTITY = 0.0
    STOCK_TYPE_I_O = str()
    State = str()

    def Stock_Data_GET(self):
        while True:
            print('Stock Master')
            choice = int(input(
                "1.insert data\n2.print data\n3.State\n11.ENTER 11 TO EXIT\nCHOSE YOUR OPERATION :- "))
            print()
            if choice == 1:
                stock_id_count = next(self.STOCK_ID)
                print("STOCK INCOMING OUTGOING ID :- ", stock_id_count)

                self.CUST_ID = int(input("ENTER CUSTOMER ID :- "))
                if self.CUST_ID not in super().Customer_Detail.keys():
                    print('PLEASE ENTER VALID CUSTOMER ID.\n')
                    work = int(input("you want to add that customer ? \n1.YES\n2.NO\nCHOSE YOUR OPERATION :- "))
                    if work == 1:
                        return Customer_Master().CUST_Data_Get()
                    return Stock_Master().Stock_Data_GET()

                self.PROD_ID = int(input("ENTER PRODUCT ID :- "))
                if self.PROD_ID not in super().Product_Detail.keys():
                    print('PLEASE ENTER VALID PRODUCT ID.\n')
                    work = int(input("you want to add that product ? \n1.YES\n2.NO\nCHOSE YOUR OPERATION :- "))
                    if work == 1:
                        return Product_Master().PRODU_GET_DATA()
                    return Stock_Master().Stock_Data_GET()
                self.STOCK_QUANTITY = float(input("ENTER THE QUANTITY THAT YOU WANT TO IN OR OUT :- "))
                state = int(input("1.DONE.\n2.RESERVE.\nCHOSE YOUR OPERATION :- "))
                if state == 1:
                    self.Product_Detail[self.PROD_ID].update({"STATE": "DONE"})
                    self.State = "DONE"
                    choice_prod_i_o = int(input("1.PRODUCT INCOMING\n2.PRODUCT OUTGOING\nCHOSE YOUR OPERATION :- "))
                    if choice_prod_i_o == 1:
                        sum_of_incoming = self.STOCK_QUANTITY + super().Product_Detail[self.PROD_ID].get(
                            "PROD_INCOMING")
                        sum_of_stock = self.STOCK_QUANTITY + super().Product_Detail[self.PROD_ID].get("PROD_STOCK")
                        super().Product_Detail[self.PROD_ID].update(
                            {"PROD_INCOMING": sum_of_incoming, "PROD_STOCK": sum_of_stock})
                        self.STOCK_TYPE_I_O = "PRODUCT INCOMING"
                    elif choice_prod_i_o == 2:
                        if self.STOCK_QUANTITY > super().Product_Detail[self.PROD_ID].get("PROD_STOCK"):
                            print('PLEASE CHECK STOCK.\n')
                            return Stock_Master().Stock_Data_GET()
                        sum_of_outgoing = self.STOCK_QUANTITY + super().Product_Detail[self.PROD_ID].get(
                            "PROD_OUT_GOING")
                        sum_of_stock = super().Product_Detail[self.PROD_ID].get(
                            "PROD_STOCK") - self.STOCK_QUANTITY
                        super().Product_Detail[self.PROD_ID].update(
                            {"PROD_OUT_GOING": sum_of_outgoing, "PROD_STOCK": sum_of_stock})
                        self.STOCK_TYPE_I_O = "PRODUCT OUTGOING"
                    else:
                        print("Enter valid option")
                else:
                    self.Product_Detail[self.PROD_ID].update({"STATE": "RESERVE"})
                    self.State = "RESERVE"
                self.Stock_Detail[stock_id_count] = {stock_id_count: stock_id_count, "CUST_ID": self.CUST_ID,
                                                     "PROD_ID": self.PROD_ID, "PROD_QUANTITY": self.STOCK_QUANTITY,
                                                     "STOCK_TYPE_I_O": self.STOCK_TYPE_I_O, "STATE": self.State}
            elif choice == 2:
                print(self.Stock_Detail)
                return Stock_Master().Stock_Data_GET()
            elif choice == 3:
                id = int(input("PROVIDE STOCK ID :- "))
                print(self.Stock_Detail.get(id))
                state = int(input("1.DONE.\n2.RESERVE.\nCHOSE YOUR OPERATION :- "))
                if state == 1:
                    self.Product_Detail[id].update({"STATE": "DONE"})
                    self.Stock_Detail[id].update({"STATE": "DONE"})
                    choice_prod_i_o = int(input("1.PRODUCT INCOMING\n2.PRODUCT OUTGOING\nCHOSE YOUR OPERATION :- "))
                    if choice_prod_i_o == 1:
                        sum_of_incoming = self.Stock_Detail[id].get("PROD_QUANTITY") + super().Product_Detail[id].get(
                            "PROD_INCOMING")
                        sum_of_stock = self.Stock_Detail[id].get("PROD_QUANTITY") + super().Product_Detail[id].get(
                            "PROD_STOCK")
                        super().Product_Detail[id].update(
                            {"PROD_INCOMING": sum_of_incoming, "PROD_STOCK": sum_of_stock})
                        self.STOCK_TYPE_I_O = "PRODUCT INCOMING"
                    elif choice_prod_i_o == 2:
                        if self.STOCK_QUANTITY > super().Product_Detail[id].get("PROD_STOCK"):
                            print('PLEASE CHECK STOCK.\n')
                            return Stock_Master().Stock_Data_GET()
                        sum_of_outgoing = self.Stock_Detail[id].get("PROD_QUANTITY") + super().Product_Detail[id].get(
                            "PROD_OUT_GOING")
                        sum_of_stock = super().Product_Detail[id].get(
                            "PROD_STOCK") - self.Stock_Detail[id].get("PROD_QUANTITY")
                        super().Product_Detail[id].update(
                            {"PROD_OUT_GOING": sum_of_outgoing, "PROD_STOCK": sum_of_stock})
                        self.STOCK_TYPE_I_O = "PRODUCT OUTGOING"
                    else:
                        print("Enter valid option")
            elif choice == 11:
                break
            else:
                print("Enter valid option")


while True:
    i = int(input(
        "1.Customer_Master\n2.Product_Master\n3.Stock_Move_Master\n11.ENTER 11 TO EXIT\nCHOSE YOUR OPERATION :- "))
    print()
    if i == 1:
        print()
        Customer_Master().CUST_Data_Get()
    elif i == 2:
        Product_Master().PRODU_GET_DATA()
        print()
    elif i == 3:
        print()
        Stock_Master().Stock_Data_GET()
    elif i == 11:
        break
print("THANK YOU......")
