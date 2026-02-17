#################################  INDEX  #########################################
# 1.	
name = ''' Hi How are you?
Starterd learning python.
It's really interesting.''' 

name[:] 
name[-10:-5]
name[3:12]
name[12:3]
name[5:6]
name[-4:-12]
name[::2]
name[::-2]

#2.	
L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
L1[:]
L1[::3]
L1[::-2]
#How to extract  value “Happy” based on index and negative index
L1.index('Happy')
L1[8]
L1[-2]
# How to check type of data in list at 4th position
type(L1[3])

# Extract values for 100, 300, 400 
L1[5:8]


#3.
L2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"]
L2[4]
L2[1:5]
L2[7]
L2[7][2]
L2[7][2:]
L2[ : 3]
L2[3:]

# #4.	From the above l2 value ‘b’ must be changed to ‘BEE’.
L2[4][1] = 'BEE'
L2

# # 5.	From l2 “BEE” has to discard.
L2[4].remove('BEE')
L2
# 6.	In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}
L2.append({'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']})
L2
# 7.	From l2 extract insect information.
L2[-1]['insect']
print(L2)

# 8.	Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2
d1 = {'a': 10, 'b': 20, 'c': 30}
L2.insert(1, d1)
L2

# 9.	Based on new l2 created here extract the value 10 from l2 dictionary.
L2[1]['a']

# 10.	
L2 =[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, 'Success', (200,300, "Hundreds")] 
L2[4][2]
L2[5][:]
L2[2][:]
L2[1:5]
L2[5]
L2[5][3:-1]
L2[-1]
L2[-4, -3]
L2[-4: -10]
L2[7][2]
L2[-7][2:]
L2[:- 3]
L2[-3:]


########################################### IF ELSE IF ###############################################
#11. 
def check_result(marks):
    if marks.isdigit():
        marks = int(marks)

        if marks > 80:
            print("You got Distinction")

        elif marks > 60:
            print("You got First Class")

        elif marks > 40:
            print("You got Second Class")

        elif marks >= 35:
            print("PASS")

        else:
            print("FAIL")
    else:
        print("Enter valid marks")


def main():
    marks = input("Enter your marks: ")
    check_result(marks)


main()


marks = input("Enter your marks: ") 
if marks.isdigit(): 
    if marks > 80: 
        print("You got Distinction") 
    elif marks > 60: 
        print("You got First Class") 
    elif marks > 40: 
        print("You got Second Class") 
    elif marks >= 35: 
        print("PASS") 
    else: 
        print("FAIL") 
else : 
    print ("Enter valid marks")



#12.

def get_input():
    salary = float(input("Enter your yearly salary in LPA: "))
    rating = input("Enter your rating (A/B/C/D): ").upper()
    return salary, rating


def calculate_increment(salary, rating):
    increment = 0

    if salary <= 5:
        if rating == 'A':
            increment = 16
        elif rating == 'B':
            increment = 12
        elif rating == 'C':
            increment = 10
        elif rating == 'D':
            increment = 6

    elif salary <= 10:
        if rating == 'A':
            increment = 14
        elif rating == 'B':
            increment = 10
        elif rating == 'C':
            increment = 8
        elif rating == 'D':
            increment = 6

    elif salary <= 15:
        if rating == 'A':
            increment = 8
        elif rating == 'B':
            increment = 6
        elif rating == 'C':
            increment = 4
        elif rating == 'D':
            increment = 0

    elif salary <= 23:
        if rating == 'A':
            increment = 7
        elif rating == 'B':
            increment = 5
        elif rating == 'C':
            increment = 4
        elif rating == 'D':
            increment = 0

    else:
        print("Range Exceeded")
        return None

    return increment


def calculate_new_salary(salary, increment):
    return salary + (salary * increment / 100)


def display_result(increment, new_salary):
    print("Increment Percentage:", increment, "%")
    print("New Salary:", round(new_salary, 2), "LPA")


def main():
    salary, rating = get_input()

    increment = calculate_increment(salary, rating)

    if increment is None:
        return

    new_salary = calculate_new_salary(salary, increment)

    display_result(increment, new_salary)


main()



#13. 
L1 = ["HR", "Finance", "Marketing", "DS"]

base_fee = 200000
hostel_fee = 200000
food_per_month = 2000
transport_per_sem = 13000


def user_input():
    subject = input("Enter Subject (HR/Finance/Marketing/DS): ")
    analytics = input("Do you want Analytics? (y/n): ")
    hostel = input("Do you want Hostel? (y/n): ")
    food_months = int(input("Enter number of months for food: "))
    transport = input("Transportation (semester/annual): ")

    return subject, analytics, hostel, food_months, transport


def course_fee(subject, analytics):
    course_fee = base_fee

    if analytics == 'y' and subject != "DS":
        course_fee += base_fee * 0.10

    elif analytics == 'y' and subject == "DS":
        print("Analytics is not applicable for DS")

    return course_fee


def food_fee(food_months):
    return food_months * food_per_month


def transport_fee(transport):
    if transport == "semester":
        return transport_per_sem * 2

    elif transport == "annual":
        return transport_per_sem * 2

    else:
        print("Invalid Option")
        return None


def display(subject, course_fee, food_fee, transport_fee, total_fee):
    print("\n----- Fee Details -----")
    print("Subject:", subject)
    print("Course Fee:", int(course_fee))
    print("Food Fee:", food_fee)
    print("Transport Fee:", transport_fee)
    print("Total Annual Cost: ₹", int(total_fee))


def main():
    subject, analytics, hostel, food_months, transport = user_input()

    if subject not in L1:
        print("Invalid Subject")
        return

    course_fee = course_fee(subject, analytics)

    if hostel == 'y':
        course_fee += hostel_fee

    food_fee = food_fee(food_months)

    transport_fee = transport_fee(transport)

    if transport_fee is None:
        return

    total_fee = course_fee + food_fee + transport_fee

    display(subject, course_fee, food_fee, transport_fee, total_fee)


main()


#14. 

def take_user_input():
    choice = input("Do you want Books (1) or Notebook (2): ")
    return choice


def calculate_price(choice):

    if choice == '1':   # BOOKS
        standard = int(input("Enter Standard: "))
        subject = input("Enter Subject: ")

        if 1 <= standard <= 4:
            new_standard = '1st-4th'
        elif 5 <= standard <= 8:
            new_standard = '5th-8th'
        elif 9 <= standard <= 10:
            new_standard = '9th-10th'
        else:
            print("Standard should be between 1 to 10")
            return None

        books_price = {
            '1st-4th': {
                'Hindi': 60, 
                'Marathi': 60, 
                'English': 80,
                'Science': 90, 
                'Maths': 100
            },
            '5th-8th': {
                'Hindi': 100, 
                'Marathi': 100, 
                'English': 100,
                'Science': 120, 
                'Maths': 140
            },
            '9th-10th': {
                'Hindi': 150, 
                'Marathi': 150, 
                'English': 150,
                'Science': 200, 
                'Maths': 250
            }
        }

        price = books_price[new_standard].get(subject)

        if price is None:
            print("Invalid subject")
            return None

        return ("Book", subject, price)


    elif choice == '2':   # NOTEBOOK

        pages = int(input("Enter Pages (100 or 200): "))
        book_type = input("Enter Book Type: ")

        if pages == 100:
            page_key = 'Pages100'
        elif pages == 200:
            page_key = 'Pages200'
        else:
            print("Invalid pages")
            return None


        notebook_price = {
            'Pages100': {
                'square': 40, 
                '4lines': 30, 
                '2lines': 20,
                'single lines': 60, 
                'A4 Notebook': 100
            },
            'Pages200': {
                'square': 70, 
                '4lines': 50, 
                '2lines': 50,
                'single lines': 100, 
                'A4 Notebook': 180
            }
        }

        price = notebook_price[page_key].get(book_type)

        if price is None:
            print("Invalid notebook type")
            return None

        return ("Notebook", book_type, price)


    else:
        print("Invalid Choice")
        return None


def final_bill(items, total):

    print("\n========= FINAL BILL =========")

    for i, item in enumerate(items, start=1):
        print(f"{i}. {item[0]} - {item[1]} : Rs.{item[2]}")

    print("------------------------------")
    print(f"Total Amount : Rs.{total}")
    print("==============================")


cart = []      
total_price = 0  

while True:

    choice = take_user_input()
    result = calculate_price(choice)

    if result:
        cart.append(result)
        total_price += result[2]
        print("Item Added Successfully ")

    more = input("\nDo you want to purchase more? (yes/no): ")

    if more != "yes":
        break


# Final Bill
if cart:
    final_bill(cart, total_price)
else:
    print("No items purchased.")


#15.
#16.


######################################## TYPE  CASTING  #####################################

#17.
a=100 

# •	Convert a to string 
str(a)

# •	Convert a to list  
list(a)  #TypeError

# •	Convert a to tuple  
tuple(a)  #TypeError

# •	Convert a to dict 
dict(a)  #TypeError

# •	Convert a to set 
set(a)  #TypeError

# •	Convert to float 
float(a)


# 8.
city = "PUNE"

# •	Convert to int  
int(city)    #ValueError

# •	Convert float
float(city)    #ValueError

# •	Convert list  
list(city)

# •	Convert tuple 
tuple(city)

# •	Convert dict 
dict(city)   #ValueError


# •	Convert set 
set(city)

 
# 9.
marks = [20,18,15,17,18] 

# •	Convert to int 
int(marks)    #TypeError

# •	Convert float 
float(marks)   #TypeError

# •	Convert list 
list(marks)

# •	Convert tuple 
tuple(marks)

# •	Convert dict 
dict(marks)    #TypeError

# •	Convert set 
set(marks)



###################################         LIST OPERATIONS       ###########################

#10. Create the empty list snames 
snames = []
print(snames)

# • Add value 20 in the list using append 
snames.append(20)
print(snames)

# • Add value 30 in the list using extend 
snames.extend([30])
print(snames)

# • Add values in the list using append 
snames.append(140)
snames.append(450)
print(snames)

# • Add value “WORK" in the list using extend 
snames.extend("WORK")
print(snames)

# • Create a new list combo having the values [1, ‘a’, ‘b’ ,2 , 3] 
combo = [1, 'a', 'b', 2, 3]
print(combo)

# • Add sname to combo using addition operator 
new_combo = combo + snames
print(new_combo)

# • Add combo to snames using append 
snames.append(combo)
print(snames)

# • Add combo to snames using extend.
snames.extend(combo)
print(snames)


#11.	Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 
l1 = [7,3]
l3 = [8,2,55,11,88,4]
l3.insert(3, l1)
l3

# 12.	Collection is the list having values [1,2,3,[‘a’, ‘b’, ‘c’], 100, ‘Nisha’, 20.50, 90.10 ] if the data is in integer or float then multiply with 5.  
collection = [1, 2, 3, ['a','b','c'], 100, 'Nisha', 20.50, 90.10]

for i in range(len(collection)):
    if isinstance(collection[i], (int, float)):
        collection[i] *= 5

print(collection)

# •	From the collection delete the record for “Nisha” 
collection.remove('Nisha')
collection

# •	Find the location of 20.50 
collection = [1, 2, 3, ['a','b','c'], 100, 'Nisha', 20.50, 90.10]
collection.index(20.50)

# 13.	Create a comprehensive list for square upto 10 
square = [i**2 for i in range(1, 11)]
print(square)

# 14.	Create the comprehensive list to find number divisible by 13 till 200
div = [i for i in range(1, 201) if i % 13 == 0]
print(div)

# 15.	Create the list which is divisible by 4 from 300 to 400  
div2 = [i for i in range(300, 401) if i % 4 == 0]
print(div2)

# 16.	Create a comprehensive list to generate list up to x, y as a number. For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]

x = 1
y = 2

x_list = list(range(x))
y_list = list(range(y))

# Then generate a new list based on all combination of x and y.
combination = [[i, j] for i in x_list for j in y_list]

print(combination)

#17.
#18.
#19.
#20.

#21.How to create empty set? 
s = set()

#22.	Create the set s1 and s2 and perform set operations like union, intersection, difference, set difference.
s1 = {1,2,3,4}
s2 = {9,7,5,4}

print(s1 | s2)      # Union
print(s1 & s2)      # Intersection
print(s1 - s2)      # Difference
print(s2 - s1)      # Set Difference

#23.	Create l2 as a list and perform set operation on s1 with l1 
l1 = [4,6,2,3]
s1 = {1,2,3}

l1_set = set(l1)

print(s1 | l1_set)
print(s1 & l1_set)
print(s1 - l1_set)

#24.	Ask user to enter the name and DOB and generate the password based on first name 4 characters and  @ddmm. For example name = SURESH and DOB = 05-05-1978 then password will be SURE@0505 

def password_ddmm(name, dob):
    first_part = name[:4].upper()      
    date_part = dob[:5].replace("-", "")  

    password = first_part + "@" + date_part
    return password


def main():
    name = input("Enter your Name: ")
    dob = input("Enter DOB (DD-MM-YYYY): ")

    password = password_ddmm(name, dob)

    print("New Password:", password)


main()

#25.	Ask user to enter the name and DOB and generate the password based on first name 4 characters and  last 4 digits of DOB or year @yyyy. For example name = SURESH and DOB = 05-05-1978 then password will be SURE@1978 

def password_year(name, dob):
    first_part = name[:4].upper()   
    year_part = dob[-4:]           

    password = first_part + "@" + year_part
    return password


def main():
    name = input("Enter your Name: ")
    dob = input("Enter DOB (DD-MM-YYYY): ")

    password = password_year(name, dob)

    print("New Password:", password)


main()


###################################### PATTERN #######################################

# 26.	Create the format mentioned here.
# *
# * *
# * * *
# * * * *
for i in range(1, 5):
    print("* " * i)



# 27.	Create the format as mentioned below:
# ****
# ***
# **
# *
for i in range(4, 0, -1):
    print("*" * i)


# 28.	Str_val = “ABCD” then create the format as mentioned below:
# A
# A B
# A B C
# A B C D
str = input ("Enter a string:")

for i in range(1, len(str)+1):
    print(" ".join(str[:i]))

# 29.	Create the format mentioned below:
# A
# BB
# CCC
# DDDD
s = input ("Enter a string:")

for i in range(len(s)):
    print(s[i] * (i+1))


# 30.	Create the format mentioned below:
# 1
# 22
# 333
# 4444
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()


# 31.	Val = “ABCD”  based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA
str = input ("Enter a string")
rev = str[::-1]

for i in range(1, len(rev)+1):
    print(rev[:i])


# 32.	Ask user to enter the string. If string is UPGRAD then output must be
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU
s = input("Enter a string: ")
rev = s[::-1]

for i in range(1, len(rev)+1):
    print(rev[:i])


# 33.	Create a list of odd numbers from 1 to 10
# 1.	Using for loop
odd = []

for i in range(1, 11):
    if i % 2 != 0:
        odd.append(i)
print(odd)

# 2.	Using comprehensive list
odd2 = [i for i in range(1, 11) if i % 2 != 0]

print(odd2)


# 34.	Create even number list using for loop from 200 to 250
even = []

for i in range(200, 251):
    if i % 2 == 0:
        even.append(i)
print(even)
