#Choose Subject 

def opt_subject():
    subjects = ["HR", "FINANCE", "MARKETING", "DS"]

    while True:
        subject = input("Enter subject HR / Finance / Marketing / DS: ").upper()

        if subject in subjects:
            return subject
        else:
            print(" Invalid choice ")



# input

def input_choice(val):
    while True:
        choice = input(val)

        if choice in ["Yes", "No"]:
            return choice
        else:
            print("Enter Yes or No")


# Monthly food

def monthly_food():
    while True:
        try:
            months = int(input("Enter months for food: "))

            if months >= 0:
                return months
            else:
                print("Months cannot be negative")

        except ValueError:
            print("Enter valid number.")



# Transport

def transport_charge():
    while True:
        transport = input("Transportation  Semester / Annual: ")

        if transport in ["Semester", "Annual"]:
            return transport
        else:
            print("Enter Semester or Annual ")


# Fee Calculation

def calculate_fees(subject, analytics, hostel, food_months, transport):

    course_fee = 200000

    # Analytics
    if analytics == "Yes" and subject != "DS":
        analytics_fee = course_fee * 0.10
    else:
        analytics_fee = 0

    # Hostel
    if hostel == "Yes":
        hostel_fee = 200000  
    else:
        hostel_fee = 0

    # Food
    food_fee = food_months * 2000

    # Transport
    if transport == "semester":
        transport_fee = 13000  
    else:
        transport_fee = 26000

    # Total
    total =  course_fee + analytics_fee + hostel_fee + food_fee + transport_fee
    

    return {
        "course": course_fee,
        "analytics": analytics_fee,
        "hostel": hostel_fee,
        "food": food_fee,
        "transport": transport_fee,
        "total": total
    }


#Show bill
def display_bill(bill):

    print("\n---------------------------------")
    print("        STUDENT' S BILL")
    print("------------------------------------")

    print(f"Course Fee        : Rs.{bill['course']}")
    print(f"Analytics Fee     : Rs.{bill['analytics']}")
    print(f"Hostel Fee        : Rs.{bill['hostel']}")
    print(f"Food Fee          : Rs.{bill['food']}")
    print(f"Transport Fee     : Rs.{bill['transport']}")

    print("-------------------------------------")
    print(f"TOTAL AMOUNT      : Rs.{bill['total']}")
    print("------------------------------------\n")


# Download bill
def save_bill(bill):

    with open("students's_bill.txt", "a") as f:

        f.write("\n--------------------------------------\n")
        f.write("        STUDENT'S BILL")
        f.write("\n--------------------------------------\n")

        f.write(f"Course Fee        : {bill['course']}\n")
        f.write(f"Analytics Fee     : {bill['analytics']}\n")
        f.write(f"Hostel Fee        : {bill['hostel']}\n")
        f.write(f"Food Fee          : {bill['food']}\n")
        f.write(f"Transport Fee     : {bill['transport']}\n")

        f.write("-------------------------------------\n")
        f.write(f"TOTAL AMOUNT      : {bill['total']}\n")
        f.write("---------------------------------------\n")



# Main Menu
def main():

    print("\n------ Student Fee System ------\n")

    subject = opt_subject()

    analytics = input_choice("Do you want Analytics? (Yes/No): ")

    if subject == "DS" and analytics == "Yes":
        print("Analytics is not available for DS")
        analytics = "No"

    hostel = input_choice("Do you want Hostel? (Yes/No): ")

    food_months = monthly_food()

    transport = transport_charge()

    # Calculate total fees
    bill = calculate_fees( subject, analytics, hostel,food_months,transport )

   
    display_bill(bill)

    #Download bill
    choice = input_choice("Do you want to download the bill? (Yes/No): ")

    if choice == "Yes":
        save_bill(bill)
        print("\n Bill downloaded as student_bill.txt")

    else:
        print("\n Bill is not saved.")

#Main Menu
main()
