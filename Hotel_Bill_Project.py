import pyodbc

# DATABASE CONNECTIVITY
class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-R8VQ8NH\\SQLEXPRESS;"
            "Database=CanteenDB;"
            "Trusted_Connection=yes;"
        )
        self.cur = self.conn.cursor()

    # Select menu items
    def fetch_menu(self):
        self.cur.execute("SELECT * FROM Menu")
        return self.cur.fetchall()

    # Select waiters
    def fetch_waiters(self):
        self.cur.execute("SELECT WaiterName FROM Waiters")
        rows = self.cur.fetchall()
        return [row[0] for row in rows]

    def close(self):
        self.conn.close()


# CUSTOMER CHOICE
class Customer:
    def select_dish(self, menu):
        while True:
            dish = input("Enter Dish Name: ")
            for key, value in menu.items():
                dish_name = value[0]
                price = value[1]
                if dish == dish_name:
                    self.dish = value[0]
                    self.price = price
                    return
            print("Invalid Dish Name! Try again.")

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


# HOTEL 
class Hotel:
    def __init__(self):
        self.db = Database()

    # Show menu
    def show_menu(self):
        rows = self.db.fetch_menu()
        self.menu = {}
        print("\n       HOTEL MENU ")
        for r in rows:
            self.menu[r[0]] = (r[1], r[2])
            print(f"{r[0]}  {r[1]:10} Rs.{r[2]}")
        print("-----------------------------")

    # Generate bill
    def generate_bill(self, table, order):
        bill = ""
        bill += "\n" + "-" * 45
        bill += "\n        HOTEL BILL"
        bill += "\n" + "-" * 45

        bill += f"\nCustomer : {order['customer']}"
        bill += f"\nTable No : {table}"
        bill += f"\nWaiter   : {order['waiter']}"    
        bill += f"\nDish     : {order['dish']}"
        bill += f"\nQuantity : {order['qty']}"
        bill += f"\nPrice    : {order['price']} Rs"

        bill += "\n" + "-" * 45
        bill += f"\nTotal Amount : {order['total']} Rs"
        bill += "\n" + "-" * 45

        return bill

    # Take order
    def take_order(self):
        table = input("\nEnter Table Number: ")

        customer_name = input ("Enter Customer Name: ")
        self.show_menu()

        # Fetch waiters 
        waiters = self.db.fetch_waiters()
        print("\nAvailable Waiters:", ", ".join(waiters))

        waiter_name = input("Enter Waiter Name: ")
        if waiter_name not in waiters:
            print("Waiter not available. Assigning default waiter:", waiters[0])
            waiter_name = waiters[0]

        cust = Customer()
        cust.select_dish(self.menu)
        cust.quantity()

        order = {
            "customer": customer_name,
            "dish": cust.dish,
            "qty": cust.qty,
            "price": cust.price,
            "total": cust.total(),
            "waiter": waiter_name
        }

        bill = self.generate_bill(table, order)
        print("\nBill Generated")
        self.print_bill(bill)

    # Print bill
    def print_bill(self, bill):
        ch = input("\nDo you want to print bill? (yes/no): ").lower()
        if ch == "yes":
            print(bill)
        else:
            print("Bill Not Printed")

    # Main program
    def run(self):
        print("HOTEL BILL PROJECT")
        while True:
            self.take_order()
            again = input("\nTake another order? (yes/no): ").lower()
            if again != "yes":
                break
        print("\nThank You! Visit Again")
        self.db.close()


# MAIN MENU
if __name__ == "__main__":
    system = Hotel()
    system.run()
