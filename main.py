import pymysql
import pymysql.cursors
import os
import sys
from dotenv import load_dotenv

#-----------------ESTABLISHING CONNECTION-----------------#

load_dotenv()

# Obtaining the credentials for access to the database
HOST = os.getenv("MYSQL_HOST")
USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
DATABASE = os.getenv("MYSQL_DATABASE")

# Connecting to the database
try:
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD,
                                 db=DATABASE, cursorclass=pymysql.cursors.DictCursor)
except:
    sys.exit("CONNECTION ERROR: Please check\n \
    * if you have entered the correct credentials in the .env file\n \
    * that the you have the permissions to access the database")

#-----------------INSERT FUNCTIONS-----------------#

# Insert/register a new customer
def insertCustomer():
    print("INSERT CUSTOMER:\n")
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    dateOfBirth = input("Enter date of birth (yyyy-mm-dd): ")
    gender = input("Enter gender: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    number = input("Enter phone number: ")

    dob = dateOfBirth.split("-")
    day, month, year = dob[2], dob[1], dob[0]

    # Storing the queries
    query_1 = "INSERT INTO Customer(First_name, Last_name, Day_of_birth, Month_of_birth, Year_of_birth, Gender, Address) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    query_2 = "INSERT INTO Customer_email VALUES(%s, %s)"
    query_3 = "INSERT INTO Customer_phone_number VALUES(%s, %s)"

    try:
        cursor.execute(query_1, (firstName, lastName,
                       day, month, year, gender, address))

        # Obtaining the Customer ID
        cursor.execute(
            "SELECT * FROM Customer ORDER BY Customer_ID DESC LIMIT 1")
        customerID = cursor.fetchone()["Customer_ID"]

        cursor.execute(query_2, (customerID, email))
        cursor.execute(query_3, (customerID, number))
    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Customer record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Customer record.\n")
    connection.commit()


# Insert/register a new employee (and developer if so)
def insertEmployee():
    print("INSERT EMPLOYEE:\n")
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    dateOfBirth = input("Enter date of birth (yyyy-mm-dd): ")
    gender = input("Enter gender: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    number = input("Enter phone number: ")
    salary = input("Enter salary: ")
    department = input("Enter department: ")
    designation = input("Enter designation: ")
    dateOfJoining = input("Enter date of joining (yyyy-mm-dd): ")

    dob = dateOfBirth.split("-")
    day, month, year = dob[0], dob[1], dob[2]

    # Storing the queries
    query_1 = "INSERT INTO Employee(First_name, Last_name, Day_of_birth, Month_of_birth, Year_of_birth, Gender, Address, Salary, Department, Designation, Date_of_joining) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    query_2 = "INSERT INTO Employee_email VALUES(%s, %s)"
    query_3 = "INSERT INTO Employee_phone_number VALUES(%s, %s)"

    try:
        cursor.execute(query_1, (firstName, lastName,
                       day, month, year, gender, address, salary, department, designation, dateOfJoining))

        # Obtaining the Employee ID
        cursor.execute(
            "SELECT * FROM Employee ORDER BY Employee_ID DESC LIMIT 1")
        employeeID = cursor.fetchone()["Employee_ID"]

        cursor.execute(query_2, (employeeID, email))
        cursor.execute(query_3, (employeeID, number))

        # Because Employee has a subclass Developer
        if department == "Developer":
            project = input("Enter project name: ")
            cursor.execute("INSERT INTO Developer VALUES(%s, %s)",
                           (employeeID, project))

    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Employee record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Employee record.\n")
    connection.commit()


# Insert a new product
def insertProduct():
    print("INSERT PRODUCT:\n")
    category = input("Enter category: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    mrp = input("Enter MRP: ")
    buyPrice = input("Enter buying price: ")
    sellPrice = input("Enter selling price: ")
    availableQuantity = input("Enter available quantity: ")

    # Storing the query
    query = "INSERT INTO Product(Category, Brand, Model, MRP, Buying_price, Selling_price, Available_quantity, In_stock) VALUES(%s, %s, %s, %s, %s, %s, %s, TRUE)"

    try:
        cursor.execute(query, (category, brand, model, mrp,
                       buyPrice, sellPrice, availableQuantity))
    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Product record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Product record.\n")
    connection.commit()


# Insert a new order and its payment
def insertOrder():
    date = input("Enter date (yyyy-mm-dd): ")
    customerID = input("Enter customer ID: ")
    productList = input("Enter space-separated list of product IDs: ")
    quantityList = input("Enter space-separated list of quantities of above products in order: ")
    supplierList = input("Enter space-separated list of suppliers of above products in order: ")
    amount = input("Enter total amount: ")
    modeOfPayment = input("Enter mode of payment: ")
    discount = input("Enter discount percentage: ")
    shippingID = input("Enter shipping company ID: ")

    productList = productList.split()
    quantityList = quantityList.split()
    supplierList = supplierList.split()

    # Storing queries
    query_1 = "SELECT * FROM Customer WHERE Customer_ID = %s"
    query_2 = "SELECT * FROM Product WHERE Product_ID = %s" # Check available quantity also
    query_3 = "SELECT * FROM Supplier WHERE Supplier_ID = %s"
    query_4 = "SELECT * FROM Shipping_company WHERE Company_ID = %s"
    query_5 = "INSERT INTO Orders VALUES(%s, %s)"
    query_6 = "INSERT INTO Items_bought VALUES(%s, %s, %s)"
    query_7 = "INSERT INTO Payment VALUES(%s, %s, %s, %s)"
    query_8 = "INSERT INTO Product_purchased VALUES(%s, %s, %s, %s)"
    query_9 = "UPDATE Product SET Available_quantity = Available_quantity - %s WHERE Product_ID = %s"
    query_10 = "UPDATE Product SET In_stock = FALSE WHERE Product_ID = %s"

    try:
        # Checking for customer
        cursor.execute(query_1, (customerID,))
        if cursor.fetchone() is None:
            print(f"\nINSERTION ERROR: Customer with ID {customerID} not found.\n")
            return
        
        # Checking each product
        i = 0
        for productID in productList:
            # Checking for product IDs and if enough products are available
            cursor.execute(query_2, (productID,))
            p = cursor.fetchone()
            if p is None or p["Available_quantity"] < int(quantityList[i]):
                print(f"\nINSERTION ERROR: Product with ID {productID} not found or sufficient quantity not available.\n")
                return

            # Checking for supplier IDs
            cursor.execute(query_3, (supplierList[i]))
            if cursor.fetchone() is None:
                print(f"\nINSERTION ERROR: Supplier with ID {supplierList[i]} not found.\n")
                return

            i += 1

        # Checking for shipping company
        cursor.execute(query_4, (shippingID,))
        if cursor.fetchone() is None:
            print(f"\nINSERTION ERROR: Shipping company with ID {shippingID} not found.\n")
            return

        # Inserting into Orders
        cursor.execute(query_5, (date, shippingID))
        cursor.execute(
            "SELECT * FROM Orders ORDER BY Order_ID DESC LIMIT 1")
        orderID = cursor.fetchone()["Order_ID"]

        # Inserting into Payment
        cursor.execute(query_7, (orderID, amount, modeOfPayment, discount))

        # Inserting into Items_bought and Product_purchased and updating Available_quantity, In_stock (if necessary)
        i = 0
        for productID in productList:
            cursor.execute(query_6, (orderID, productID, quantityList[i]))
            cursor.execute(query_8, (productID, customerID, orderID, supplierList[i]))
            cursor.execute(query_9, (quantityList[i],))
            cursor.execute(query_2, (productID,))
            if cursor.fetchone()["Available_quantity"] == 0:
                cursor.execute(query_10, (productID,))

            i += 1
    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Order record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Order record.\n")
    connection.commit()


# Insert a new supplier
def insertSupplier():
    print("INSERT SUPPLIER:\n")
    company = input("Enter company name: ")
    email = input("Enter email: ")
    number = input("Enter phone number: ")

    query_1 = "INSERT INTO Supplier(Company) VALUES(%s)"
    query_2 = "INSERT INTO Supplier_email VALUES(%s, %s)"
    query_3 = "INSERT INTO Supplier_contact_number VALUES(%s, %s)"

    try:
        cursor.execute(query_1, (company,))

        # Obtaining the Supplier ID
        cursor.execute(
            "SELECT * FROM Supplier ORDER BY Supplier_ID DESC LIMIT 1")
        supplierID = cursor.fetchone()["Supplier_ID"]

        cursor.execute(query_2, (supplierID, email))
        cursor.execute(query_3, (supplierID, number))
    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Supplier record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Supplier record.\n")
    connection.commit()


# Insert a new shipping company
def insertShippingCompany():
    print("INSERT SHIPPING COMPANY:\n")
    company = input("Enter company name: ")
    email = input("Enter email: ")
    numberList = input("Enter list of space-separated phone numbers: ")

    query_1 = "INSERT INTO Shipping_company(Company_name) VALUES(%s)"
    query_2 = "INSERT INTO Shipping_company_email VALUES(%s, %s)"
    query_3 = "INSERT INTO Shipping_company_contact_number VALUES(%s, %s)"

    try:
        cursor.execute(query_1, (company,))

        # Obtaining the Shipping Company ID
        cursor.execute(
            "SELECT * FROM Shipping_company ORDER BY Company_ID DESC LIMIT 1")
        companyID = cursor.fetchone()["Company_ID"]

        cursor.execute(query_2, (companyID, email))
        for number in numberList.split():
            cursor.execute(query_3, (companyID, number))
    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Shipping Company record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Shipping Company record.\n")
    connection.commit()


# Inserting a new review
def insertReview():
    print("ENTER REVIEW:\n")
    productID = input("Enter product ID: ")
    customerID = input("Enter customer ID: ")
    stars = input("Enter stars: ")
    content = input("Enter content: ")

    # Storing the queries
    query_1 = "SELECT * FROM Product WHERE Product_ID = %s"
    query_2 = "SELECT * FROM Customer WHERE Customer_ID = %s"
    query_3 = "INSERT INTO Review VALUES(%s, %s, %s, %s)"
    query_4 = "SELECT * FROM Product_purchased WHERE Product_ID = %s AND Customer_ID = %s"

    try:
        # Checking if product ID exists
        cursor.execute(query_1, (productID,))
        if cursor.fetchone() is None:
            print(f"\nINSERTION ERROR: Product with ID {productID} not found.\n")
            return

        # Checking if customer ID exists
        cursor.execute(query_2, (customerID,))
        if cursor.fetchone() is None:
            print(f"\nINSERTION ERROR: Customer with ID {customerID} not found.\n")
            return

        # Checking if customer ordered the product
        cursor.execute(query_4, (productID, customerID))
        if cursor.fetchone() is None:
            print(f"\nINSERTION ERROR: Customer with ID {customerID} did not order product with product ID {productID}.\n")
            return

        cursor.execute(query_3, (productID, customerID, stars, content))
    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Review record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Review record.\n")
    connection.commit()

#-----------------DELETE FUNCTIONS-----------------#

#-----------------UPDATE FUNCTIONS-----------------#

#-----------------VIEW FUNCTIONS-----------------#

#-----------------FUNCTIONAL REQUIREMENTS-----------------#

#-----------------MAIN LOOP-----------------#

# Creating a cursor to execute queries
with connection.cursor() as cursor:
    insertOrder()

# Closing the connection
connection.close()
