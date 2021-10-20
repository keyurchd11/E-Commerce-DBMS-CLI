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
    pass


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
    pass

#-----------------DELETE FUNCTIONS-----------------#

#-----------------VIEW FUNCTIONS-----------------#

#-----------------MAIN LOOP-----------------#


# Creating a cursor to execute queries
with connection.cursor() as cursor:
    insertShippingCompany()

# Closing the connection
connection.close()
