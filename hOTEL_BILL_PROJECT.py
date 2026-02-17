import pyodbc


#DATABASE

class Database:

    def __init__(self):

        self.conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-R8VQ8NH\\SQLEXPRESS;"
            "Database=CanteenDB;"
            "Trusted_Connection=yes;"
        )

        self.cur = self.conn.cursor()

    # FETCH MENU
    def fetch_menu(self):

        self.cur.execute("SELECT * FROM Menu")
        return self.cur.fetchall()


    def close(self):
        self.conn.close()



# CUSTOMER CHOICE

class Customer:

    def select_dish(self, menu):

        while True:

            try:
                self.choice = int(input("Enter Dish ID: "))

                if self.choice in menu:
                    self.dish = menu[self.choice][0]
                    self.price = menu[self.choice][1]
                    return
                else:
                    print("Invalid Dish ID!")

            except ValueError:
                print("Enter numbers only!")


    def quantity(self):

        while True:

            try:
                self.qty = int(input("Enter Quantity: "))

                if self.qty > 0:
                    return
                else:
                    print("Quantity must be > 0")

            except ValueError:
                print("Enter valid number")


    def total(self):
        return self.price * self.qty



#  SYSTEM 

class HotelSystem:

    def __init__(self):

        self.db = Database()


    # Show Menu
    def show_menu(self):

        rows = self.db.fetch_menu()

        self.menu = {}

        print("\n------ HOTEL MENU ------")

        for r in rows:

            self.menu[r[0]] = (r[1], r[2])

            print(f"{r[0]}  {r[1]:10} Rs.{r[2]}")

        print("-----------------------------")


    # Generate Bill
    def generate_bill(self, table, order):

        bill = ""
        bill += "\n" + "-" * 45
        bill += "\n  HOTEL"
        bill += "\n" + "-" * 45

        bill += f"\nTable No : {table}"
        bill += f"\nDish     : {order['dish']}"
        bill += f"\nQuantity : {order['qty']}"
        bill += f"\nPrice    : {order['price']} Rs"

        bill += "\n" + "-" * 45
        bill += f"\nTotal Amount : {order['total']} Rs"
        bill += "\n" + "-" * 45

        return bill


    # Take Order
    def take_order(self):

        table = input("\nEnter Table Number: ")

        self.show_menu()

        cust = Customer()

        cust.select_dish(self.menu)
        cust.quantity()

        order = {
            "dish": cust.dish,
            "qty": cust.qty,
            "price": cust.price,
            "total": cust.total()
        }

        bill = self.generate_bill(table, order)

        print("\n Bill Generated ")

        self.print_bill(bill)


    # Print Bill
    def print_bill(self, bill):

        ch = input("\nDo you want to print bill? (yes/no): ")

        if ch == "yes":
            print(bill)
        else:
            print("Bill Not Printed")


    # Main Program
    def run(self):

        print("HOTEL BILL PROJECT")

        while True:

            self.take_order()

            again = input("\nTake another order? (yes/no): ")

            if again != "yes":
                break

        print("\nThank You! Visit Again ")

        self.db.close()



# MAIN MENU

if __name__ == "__main__":

    system = HotelSystem()
    system.run()
