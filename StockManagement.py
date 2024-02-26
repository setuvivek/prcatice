class Customer:
    def __init__(self):
        self.id_cus = 0
        self.data_cus = []
        self.pan_set = set()

    def get_cus_info(self):
        while True:
            print("\n\t\t\t--- WELCOME TO CUSTOMER ---")
            q = input("\nDo you want to quit? [y/n]: ").lower()
            if q == 'y':
                print("Thank you for your valuable time. Exiting.")
                break

            pan_number = input("Enter PAN number: ")
            if pan_number in self.pan_set:
                print("PAN number already exists. Enter correct PAN number")
                continue

            self.id_cus += 1
            name = input("Enter your Name: ")
            type_cust = input("Enter your type: ")

            self.data_cus.append((self.id_cus, pan_number, {'pan_number': pan_number, 'name_cus': name, 'type_cus': type_cust}))
            self.pan_set.add(pan_number)
            print("Data saved!")

            print(self.data_cus)
            return self.data_cus, self.id_cus

    # def search_cus(self):
    #     if self.data_cus:
    #         print("Customer data exists.")


class Product:
    def __init__(self):
        self.data_pro = {}
        self.product_id = 0

    def get_info_pro(self):
        while True:
            print("\n\t\t\t--- WELCOME TO PRODUCT ---")

            q = input("\nDo you want to quit? (y/n): ").lower()
            if q == 'y':
                print("Thank you for your valuable time. Exiting.")
                break

            self.product_id += 1
            name = input("Enter Product Name :: ")

            while name in self.data_pro:
                ask = input(f"\nDo you still want to add {name} product? [y/n]: ").lower()
                if ask == 'n':
                    print("OKAY, GOODBYE.")
                    break

                if ask == 'y':
                    print("\n---\tCurrent Product Info\t---")
                    product = self.data_pro[name]
                    print(product)

                    continue

                else:
                    print("Input valid option, choose between 'y' for yes or 'n' for no.")
                    continue

            self.data_pro[name] = {
                'product_id': self.product_id,
                'code': input("Enter Product Code: "),
                'name': name,
                'incoming': 0,
                'outgoing': 0,
                'onhand': 0
            }
            if name not in self.data_pro:
                self.product_id += 1
                print("Product Data Saved!")

            print(self.data_pro)
        return self.data_pro


class Stock_Move(Product):
    def __init__(self):
        super().__init__()
        self.display = []

    def stock_info(self):
        while True:
            check = int(input("\nWhich customer you want to search?\nEnter Customer id : "))

            # Check if customer ID exists in customer data
            found = False
            for customer in customer_o.data_cus:
                if customer[0] == check:
                    found = True
                    break

            if not found:
                print("Customer ID not found. Please create a customer first.")
                return

            print(f"Customer ID Found: {check}")

            while True:
                product_id = int(input("Enter Product ID: "))
                product_found = False
                for product in product_o.data_pro.values():
                    if product['product_id'] == product_id:
                        product_found = True
                        product_data = product
                        break

                if not product_found:
                    create = input("Product ID not found. Create product? (y/n): ").lower()
                    if create == 'y':
                        product_o.get_info_pro()
                    else:
                        break
                else:
                    # product_data = product
                    product_name = product_data['name']
                    product_code = product_data['code']
                    current_stock = product_data['onhand']
                    # incoming

                    print(f"\nProduct Name: {product_name}\nProduct Code: {product_code}\nCurrent Stock: {current_stock}")

                    while True:
                        operation = int(input("\nWhich Product operation you want to perform?\n1.incoming\n2.outgoing\n0.Back to Admin Panel\nEnter operation number here: "))

                        if operation == 1:
                            incoming_quantity = int(input("\nEnter Incoming Quantity: "))
                            product['incoming'] = incoming_quantity
                            product['onhand'] += incoming_quantity
                            print(f"New stock: {product['onhand']}")

                        elif operation == 2:
                            outgoing_quantity = int(input("Enter Outgoing Quantity: "))

                            if outgoing_quantity > product['onhand']:
                                print("Outgoing quantity cannot exceed current stock.")
                            else:
                                product['outgoing'] = outgoing_quantity
                                product['onhand'] -= outgoing_quantity
                                print(f"New stock: {product['onhand']}")

                        elif operation == 0:
                            admin_o.operations()
                            break


                        else:
                            print("Invalid operation. Please enter '1' for incoming, '2' for outgoing, or '0' for Admin Panel.")
                break
        # self.display.append(check)
    # print(Product().data_pro)


class Admin:
    def __init__(self):
        self.client = input("Enter Your Name AS A ADMIN : ").upper()

    # def client_admin(self):
    #     print(f"\n\t\t\t--- WELCOME TO ADMIN PANEL {self.client} ---")

    def operations(self):
        while True:
            print(f"\n\t\t\t--- WELCOME TO ADMIN PANEL {self.client} ---")
            print("\nWhich operation you want to perform ?\n")
            print("1 : Add Customer")
            print("2 : Add Product")
            print("3 : Display all data")
            print("4 : Stock Move")
            print("0 : Quit")
            client = int(input("Enter Operation number here - "))

            if client == 0:
                print(f"{self.client}, Thank you for your valuable time. Visit Again!")
                exit()

            elif client == 1:
                customer_o.get_cus_info()

            elif client == 2:
                product_o.get_info_pro()

            elif client == 3:
                print("Customer Data:")
                print(customer_o.data_cus)
                print("\nProduct Data:")
                print(product_o.data_pro)

            elif client == 4:
                stock_o.stock_info()

            else:
                print(f"Uh-Oh {self.client}, It is an Invalid option. Please enter a valid number.")
                break


customer_o = Customer()
product_o = Product()
stock_o = Stock_Move()
admin_o = Admin()

# admin_o.client_admin()
admin_o.operations()
