
class Customer:
    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Type: {self.customer_type}")
        print(f"PAN: {self.pan}")
    #
    # customer1 = workbook['customer']
class Product:
    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Incoming: {self.incoming}")
        print(f"Outgoing: {self.outgoing}")

class Stock:
    def display_info(self):
        print(f"Stock ID: {self.stock_id}")
        print(f"Product ID: {self.product.product_id}")
        print(f"Product Name: {self.product.name}")
        print(f"Customer ID: {self.customer.customer_id}")
        print(f"Quantity: {self.quantity}")
        print(f"Stock Type: {self.stock_type}")

customer_dict = {}
product_dict = {}
stock_dict = {}
summary = ""

while True:
    choice = input("Enter 'C' for Customer, 'P' for Product, 'S' for Stock, 'R' for Report, or 'Q' to quit: ")

    if choice == 'Q':
        break

    if choice not in ['C', 'P', 'S', 'F', 'R']:
        print("Invalid choice. Please enter 'C', 'P', 'S', 'R', or 'Q' to quit.")
    else:
        if choice == 'C':
            customer_id = None
            while True:
                try:
                    customer_id = int(input("Enter Customer ID: "))
                    if customer_id in customer_dict:
                        print("Error: Customer ID must be unique.")
                    else:
                        break
                except ValueError:
                    print("Error: Customer ID must be an integer.")

            customer_name = input("Enter Customer Name: ")

            customer_type = None
            while True:
                customer_type = input("Enter Customer Type (customer/vendor): ")
                if customer_type.lower() in ['customer', 'vendor']:
                    break
                else:
                    print("Error: Invalid Customer Type. Please enter 'customer' or 'vendor'.")

            customer_pan = None
            while True:
                customer_pan = input("Enter Customer PAN: ")
                if customer_pan.isalnum() and customer_pan not in [customer.pan for customer in customer_dict.values()]:
                    break
                else:
                    print("Error: Customer PAN must be alphanumeric and unique.")

            customer = Customer()
            customer.customer_id = customer_id
            customer.name = customer_name
            customer.customer_type = customer_type
            customer.pan = customer_pan
            customer_dict[customer_id] = customer

            customer_dict[customer_id] = customer

            summary += f"\nCustomer ID: {customer_id}, Name: {customer_name}, Type: {customer_type}, PAN: {customer_pan}"

        elif choice == 'P':
            product_id = None
            while True:
                try:
                    product_id = int(input("Enter product ID: "))
                    if product_id in product_dict:
                        print("Error: product ID must be unique.")
                    else:
                        break
                except ValueError:
                    print("Error:product ID must be an integer.")


            product_name = str(input("Enter product name: "))

            product_incoming = int(input("Enter Incoming Product: "))
            product_outgoing = int(input("Enter Outgoing Product: "))
            product_onhand = product_incoming - product_outgoing

            # if product_onhand not in int:
            # break
            # else:
            print(product_onhand)

            product = Product()
            product.product_id = product_id
            product.name = product_name
            product.incoming = product_incoming
            product.outgoing = product_outgoing
            product_dict[product_id] = product
            product_dict[product_id] = product
            summary += f"\nProduct ID: {product_id}, Name: {product_name}, Incoming: {product_incoming}, Outgoing: {product_outgoing}, Onhand: {product_onhand}"


        elif choice == 'S':
            if not product_dict:
                print("Error: Product details are required before creating Stock.")
            else:
                stock_id = int(input("Enter Stock ID: "))
                product_id = None

                while True:
                    try:
                        product_id = int(input("Enter Product ID: "))
                        if product_id not in product_dict:
                            print("Error: Product ID does not exist.")
                        else:
                            break
                    except ValueError:
                        print("Error: Product ID must be an integer.")
                customer_id = None
                while True:
                    try:
                        customer_id = str(input("Enter customer id: "))
                        if customer_id in customer_dict:
                            print("Error: customer id already exists.")
                        else:
                            break
                    except ValueError:
                                print("Error: id can't be entered.")
                quantity = int(input("Enter Stock Quantity: "))

                while True:
                    stock_type = input("Enter Stock Type (incoming/outgoing): ")
                    if stock_type in ['incoming', 'outgoing']:
                        break
                    else:
                        print("Invalid stock type")
                # if stock_type == "incoming":
                # print(product_onhand+quantity)
                # elif stock_type == "outgoing":
                # print(product_onhand-quantity)

                # if stock_type == 'incoming':
                #     print(product_onhand+product_incoming)
                # elif stock_type == 'outgoing':
                #     print(product_onhand - product_outgoing)


                    stock = Stock()
                    stock.stock_id = stock_id
                    stock.product = product_dict.get(product_id)
                    stock.customer = customer_dict.get(customer_id)
                    stock.quantity = quantity
                    stock.stock_type = stock_type
                    stock_dict[stock_id] = stock
                        #stock_dict[stock_id] = stock
            summary += f"\nStock ID: {stock_id}, Product ID: {product_id}, Customer ID: {customer_id}, Quantity: {quantity}, Stock Type: {stock_type},"


        elif choice == 'R':
            # stock_id = int(input("Enter Stock ID to generate the report: "))
            # if stock_id not in stock_dict:
            # print("Error: Stock ID not found.")
            # else:
            # stock = stock_dict[stock_id]
            # stock.display_info()
            # summary += f"\nReport for Stock ID {stock_id}:\n"
            # summary += f"{stock.product.name}, {stock.quantity} {stock.stock_type}\n"
            if quantity > product_onhand and stock_type == 'outgoing':
                print("Error:you not have the enough quantity for outgoing")
            elif quantity > product_onhand and stock_type == 'incoming':
                print(product_onhand + quantity)
            # elif quantity < product_onhand and stock_type == 'incoming':
            #     print(product_incoming + quantity)
            elif quantity > product_onhand and stock_type == 'incoming':
                print(product_incoming + quantity)
            elif quantity > product_onhand and stock_type == 'outgoing':
                print(product_onhand-product_outgoing)
            #summary += f"Final Result: {stock.quantity} {stock.stock_type} remaining in stock.\n"
            elif quantity < product_onhand and stock_type == "outgoing":
                print(product_onhand-quantity)


            summary += f"\nFinal Result:{quantity} {stock_type} in stock.\n"

        elif choice == 'F':
            print("Summary of Entered Data:")
            print(summary)

