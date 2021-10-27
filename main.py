import pymysql
import pymysql.cursors
import os
import sys
import subprocess as sp
import time
from tabulate import tabulate
from datetime import date
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
    day, month, year = dob[2], dob[1], dob[0]

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
    supplierID = input("Enter supplier ID: ")
    mrp = input("Enter MRP: ")
    buyPrice = input("Enter buying price: ")
    sellPrice = input("Enter selling price: ")
    availableQuantity = input("Enter available quantity: ")
    
    boolVar = None
    if int(availableQuantity) <= 0:
        print("\nINSERTION ERROR: Available quantity must be more than 0.\n")
        return

    # Storing the queries
    query_1 = "SELECT * FROM Supplier WHERE Supplier_ID = %s"
    query_2 = "INSERT INTO Product(Category, Brand, Model, Supplier_ID, MRP, Buying_price, Selling_price, Available_quantity, In_stock) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, TRUE)"

    try:
        # Checking for supplier ID
        cursor.execute(query_1, (supplierID,))
        if cursor.fetchone() is None:
            print(f"\nINSERTION ERROR: Supplier with ID {supplierID} not found.\n")
            return

        cursor.execute(query_2, (category, brand, model, supplierID, mrp,
                       buyPrice, sellPrice, availableQuantity))
    except Exception as e:
        print(f"\nINSERTION ERROR: Failed to insert Product record - {e}\n")
        return

    # Committing the insertion made
    print("\nSUCCESS: Successfully inserted Product record.\n")
    connection.commit()


# Insert a new order and its payment
def insertOrder():
    print("ENTER ORDER:\n")
    date = input("Enter date (yyyy-mm-dd): ")
    customerID = input("Enter customer ID: ")
    productList = input("Enter space-separated list of product IDs: ")
    quantityList = input("Enter space-separated list of quantities of above products in order: ")
    amount = input("Enter total amount: ")
    modeOfPayment = input("Enter mode of payment: ")
    discount = input("Enter discount percentage: ")
    shippingID = input("Enter shipping company ID: ")

    productList = productList.split()
    quantityList = quantityList.split()
    supplierList = []

    # Storing queries
    query_1 = "SELECT * FROM Customer WHERE Customer_ID = %s"
    query_2 = "SELECT * FROM Product WHERE Product_ID = %s"
    query_4 = "SELECT * FROM Shipping_company WHERE Company_ID = %s"
    query_5 = "INSERT INTO Orders(Order_date, Shipping_company_ID) VALUES(%s, %s)"
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

            # Storing supplier ID
            supplierList.append(str(p["Supplier_ID"]))
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
            cursor.execute(query_9, (quantityList[i], productID))
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

# Deleting a customer
def deleteCustomer():
    print("DELETE CUSTOMER:\n")
    customerID = input("Enter ID of customer to be deleted: ")

    query_1 = "SELECT * FROM Customer WHERE Customer_ID = %s"
    query_2 = "DELETE FROM Customer WHERE Customer_ID = %s"

    try:
        # Checking if customer ID exists
        cursor.execute(query_1, (customerID,))
        if cursor.fetchone() is None:
            print(f"\nDELETION ERROR: Customer with ID {customerID} not found.\n")
            return

        cursor.execute(query_2, (customerID,))
    except Exception as e:
        print(f"\nDELETION ERROR: Failed to delete Customer record - {e}\n")
        return

    # Committing the deletion made
    print("\nSUCCESS: Successfully deleted Customer record.\n")
    connection.commit()


# Deleting an employee
def deleteEmployee():
    print("DELETE EMPLOYEE:\n")
    employeeID = input("Enter ID of employee to be deleted: ")

    query_1 = "SELECT * FROM Employee WHERE Employee_ID = %s"
    query_2 = "DELETE FROM Employee WHERE Employee_ID = %s"

    try:
        # Checking if employee ID exists
        cursor.execute(query_1, (employeeID,))
        if cursor.fetchone() is None:
            print(f"\nDELETION ERROR: Employee with ID {employeeID} not found.\n")
            return

        cursor.execute(query_2, (employeeID,))
    except Exception as e:
        print(f"\nDELETION ERROR: Failed to delete Employee record - {e}\n")
        return

    # Committing the deletion made
    print("\nSUCCESS: Successfully deleted Employee record.\n")
    connection.commit()


# Deleting a product
def deleteProduct():
    print("DELETE PRODUCT:\n")
    productID = input("Enter ID of product to be deleted: ")

    query_1 = "SELECT * FROM Product WHERE Product_ID = %s"
    query_2 = "DELETE FROM Product WHERE Product_ID = %s"

    try:
        # Checking if product ID exists
        cursor.execute(query_1, (productID,))
        if cursor.fetchone() is None:
            print(f"\nDELETION ERROR: Product with ID {productID} not found.\n")
            return

        cursor.execute(query_2, (productID,))
    except Exception as e:
        print(f"\nDELETION ERROR: Failed to delete Product record - {e}\n")
        return

    # Committing the deletion made
    print("\nSUCCESS: Successfully deleted Product record.\n")
    connection.commit()


# Deleting a supplier
def deleteSupplier():
    print("DELETE SUPPLIER:\n")
    supplierID = input("Enter ID of supplier to be deleted: ")

    query_1 = "SELECT * FROM Supplier WHERE Supplier_ID = %s"
    query_2 = "DELETE FROM Supplier WHERE Supplier_ID = %s"

    try:
        # Checking if supplier ID exists
        cursor.execute(query_1, (supplierID,))
        if cursor.fetchone() is None:
            print(f"\nDELETION ERROR: Supplier with ID {supplierID} not found.\n")
            return

        cursor.execute(query_2, (supplierID,))
    except Exception as e:
        print(f"\nDELETION ERROR: Failed to delete Supplier record - {e}\n")
        return

    # Committing the deletion made
    print("\nSUCCESS: Successfully deleted Supplier record.\n")
    connection.commit()


# Deleting a shipping company
def deleteShippingCompany():
    print("DELETE SHIPPING COMPANY:\n")
    shippingID = input("Enter ID of shipping company to be deleted: ")

    query_1 = "SELECT * FROM Shipping_company WHERE Company_ID = %s"
    query_2 = "DELETE FROM Shipping_company WHERE Company_ID = %s"

    try:
        # Checking if shipping company ID exists
        cursor.execute(query_1, (shippingID,))
        if cursor.fetchone() is None:
            print(f"\nDELETION ERROR: Shipping company with ID {shippingID} not found.\n")
            return

        cursor.execute(query_2, (shippingID,))
    except Exception as e:
        print(f"\nDELETION ERROR: Failed to delete Shipping Company record - {e}\n")
        return

    # Committing the deletion made
    print("\nSUCCESS: Successfully deleted Shipping Company record.\n")
    connection.commit()


# Deleting an order
def deleteOrder():
    print("DELETE ORDER:\n")
    orderID = input("Enter ID of order to be deleted: ")

    query_1 = "SELECT * FROM Orders WHERE Order_ID = %s"
    query_2 = "DELETE FROM Orders WHERE Order_ID = %s"

    try:
        # Checking if order ID exists
        cursor.execute(query_1, (orderID,))
        if cursor.fetchone() is None:
            print(f"\nDELETION ERROR: Order with ID {orderID} not found.\n")
            return

        cursor.execute(query_2, (orderID,))
    except Exception as e:
        print(f"\nDELETION ERROR: Failed to delete Order record - {e}\n")
        return

    # Committing the deletion made
    print("\nSUCCESS: Successfully deleted Order record.\n")
    connection.commit()


# Deleting a review
def deleteReview():
    print("DELETE REVIEW:\n")
    productID = input("Enter product ID of review to be deleted: ")
    customerID = input("Enter customer ID of review to be deleted: ")

    query_1 = "SELECT * FROM Review WHERE Product_ID = %s AND Customer_ID = %s"
    query_2 = "DELETE FROM Review WHERE Product_ID = %s AND Customer_ID = %s"

    try:
        # Checking if review exists
        cursor.execute(query_1, (productID, customerID))
        if cursor.fetchone() is None:
            print(f"\nDELETION ERROR: Review with product ID {productID} and customer ID {customerID} not found.\n")
            return

        cursor.execute(query_2, (productID, customerID))
    except Exception as e:
        print(f"\nDELETION ERROR: Failed to delete Review record - {e}\n")
        return

    # Committing the deletion made
    print("\nSUCCESS: Successfully deleted Review record.\n")
    connection.commit()

#-----------------UPDATE FUNCTIONS-----------------#

# Updating a customer
def updateCustomer():
    print("UPDATE CUSTOMER:\n")
    print("Press Enter for any attribute you do not wish to update.\n")
    customer_ID = input("Enter ID of customer to be updated: ")

    cursor.execute("SELECT * FROM Customer WHERE Customer_ID = %s", (customer_ID,))
    row = cursor.fetchone()
    if row is None:
        print(f"\nUPDATION ERROR: Customer with ID {customer_ID} not found.\n")
        return

    firstName = input("Enter new first name: ")
    if firstName !=  "": row["First_name"] = firstName
    lastName = input("Enter new last name: ")
    if lastName != "": row["Last_name"] = lastName
    date = input("Enter new date of birth (yyyy-mm-dd): ")
    gender = input("Enter new gender: ")
    if gender != "": row["Gender"] = gender
    address = input("Enter new address: ")
    if address != "": row["Address"] = address
    email = input("Enter new email: ")
    number = input("Enter new number: ")

    if date != "":
        date = date.split("-")
        row["Day_of_birth"], row["Month_of_birth"], row["Year_of_birth"] = date[2], date[1], date[0]

    # Storing queries
    query_1 = "UPDATE Customer SET First_name = %s, Last_name = %s, Day_of_birth = %s, Month_of_birth = %s, Year_of_birth = %s, Gender = %s, Address = %s WHERE Customer_ID = %s"
    query_2 = "UPDATE Customer_email SET Email = %s WHERE Customer_ID = %s"
    query_3 = "UPDATE Customer_phone_number SET Number = %s WHERE Customer_ID = %s"

    try:
        cursor.execute(query_1, (row["First_name"], row["Last_name"], row["Day_of_birth"], row["Month_of_birth"], row["Year_of_birth"], row["Gender"], row["Address"], customer_ID))

        if email != "":
            cursor.execute(query_2, (email, customer_ID))
        if number != "":
            cursor.execute(query_3, (number, customer_ID))

    except Exception as e:
        print(f"\nUPDATION ERROR: Failed to update Customer record - {e}\n")
        return

    # Committing the updation made
    print("\nSUCCESS: Successfully updated Customer record.\n")
    connection.commit()


# Updating an employee
def updateEmployee():
    print("UPDATE EMPLOYEE:\n")
    print("Press Enter for any attribute you do not wish to update.\n")
    employee_ID = input("Enter ID of employee to be updated: ")

    cursor.execute("SELECT * FROM Employee WHERE Employee_ID = %s", (employee_ID,))
    row = cursor.fetchone()
    if row is None:
        print(f"\nUPDATION ERROR: Customer with ID {employee_ID} not found.\n")
        return

    firstName = input("Enter new first name: ")
    if firstName !=  "": row["First_name"] = firstName
    lastName = input("Enter new last name: ")
    if lastName != "": row["Last_name"] = lastName
    date = input("Enter new date of birth (yyyy-mm-dd): ")
    gender = input("Enter new gender: ")
    if gender != "": row["Gender"] = gender
    address = input("Enter new address: ")
    if address != "": row["Address"] = address
    salary = input("Enter new salary: ")
    if salary != "": row["Salary"] = salary
    department = input("Enter new department: ") # Check for removal from developer
    oldDepartment = row["Department"]
    if department != "": row["Department"] = department
    designation = input("Enter new designation: ")
    if designation != "": row["Designation"] = designation
    dateOfJoining = input("Enter new date of joining (yyyy-mm-dd): ")
    if dateOfJoining != "": row["Date_of_joining"] = dateOfJoining
    email = input("Enter new email: ")
    number = input("Enter new number: ")

    if date != "":
        date = date.split("-")
        row["Day_of_birth"], row["Month_of_birth"], row["Year_of_birth"] = date[2], date[1], date[0]

    # Storing queries
    query_1 = "UPDATE Employee SET First_name = %s, Last_name = %s, Day_of_birth = %s, Month_of_birth = %s, Year_of_birth = %s, Gender = %s, Address = %s, Salary = %s, Department = %s, Designation = %s, Date_of_joining = %s WHERE Employee_ID = %s"
    query_2 = "UPDATE Employee_email SET Email = %s WHERE Employee_ID = %s"
    query_3 = "UPDATE Employee_phone_number SET Number = %s WHERE Employee_ID = %s"

    try:
        cursor.execute(query_1, (row["First_name"], row["Last_name"], row["Day_of_birth"], row["Month_of_birth"], row["Year_of_birth"], row["Gender"], row["Address"], row["Salary"], row["Department"], row["Designation"], row["Date_of_joining"], employee_ID))

        if email != "":
            cursor.execute(query_2, (email, employee_ID))
        if number != "":
            cursor.execute(query_3, (number, employee_ID))

        # Accounting for the Developer subclass
        if oldDepartment != row["Department"]:
            if oldDepartment == "Developer":
                cursor.execute("DELETE FROM Developer WHERE Employee_ID = %s", (employee_ID,))
            elif row["Department"] == "Developer":
                project = input("Enter project name: ")
                cursor.execute("INSERT INTO Developer VALUES(%s, %s)",
                           (employee_ID, project))
        
        elif row["Department"] == "Developer":
            project = input("Enter new project name: ")
            cursor.execute("UPDATE Developer SET Project_name = %s WHERE Employee_ID = %s", (project, employee_ID))

    except Exception as e:
        print(f"\nUPDATION ERROR: Failed to update Employee record - {e}\n")
        return

    # Committing the updation made
    print("\nSUCCESS: Successfully updated Employee record.\n")
    connection.commit()


# Updating a product
def updateProduct():
    print("UPDATE PRODUCT:\n")
    print("Press Enter for any attribute you do not wish to update.\n")
    product_ID = input("Enter ID of product to be updated: ")

    cursor.execute("SELECT * FROM Product WHERE Product_ID = %s", (product_ID,))
    row = cursor.fetchone()
    if row is None:
        print(f"\nUPDATION ERROR: Product with ID {product_ID} not found.\n")
        return

    category = input("Enter new category: ")
    if category !=  "": row["Category"] = category
    brand = input("Enter new brand: ")
    if brand != "": row["Brand"] = brand
    model = input("Enter new model: ")
    if model != "": row["Model"] = model
    supplierID = input("Enter new supplier ID: ")
    if supplierID != "": row["Supplier_ID"] = supplierID
    mrp = input("Enter new MRP: ")
    if mrp != "": row["MRP"] = mrp
    buyPrice = input("Enter new buying price: ")
    if buyPrice != "": row["Buying_price"] = buyPrice
    sellPrice = input("Enter new selling price: ")
    if sellPrice != "": row["Selling_price"] = sellPrice
    availableQuantity = input("Enter new available quantity: ")
    if availableQuantity != "": row["Available_quantity"] = availableQuantity

    row["In_stock"] = "1"
    if int(row["Available_quantity"]) <= 0:
        row["In_stock"] = "0"

    # Storing queries
    query_1 = "SELECT * FROM Supplier WHERE Supplier_ID = %s"
    query_2 = "UPDATE Product SET Category = %s, Brand = %s, Model = %s, Supplier_ID = %s, MRP = %s, Buying_price = %s, Selling_price = %s, Available_quantity = %s, In_stock = %s WHERE Product_ID = %s"

    # Checking whether supplier ID exists
    cursor.execute(query_1, (row["Supplier_ID"],))
    if cursor.fetchone() is None:
        print(f"\nUPDATION ERROR: Supplier with ID {supplierID} not found.\n")
        return

    try:
        cursor.execute(query_2, (row["Category"], row["Brand"], row["Model"], row["Supplier_ID"], row["MRP"], row["Buying_price"], row["Selling_price"], row["Available_quantity"], row["In_stock"], product_ID))
    except Exception as e:
        print(f"\nUPDATION ERROR: Failed to update Product record - {e}\n")
        return

    # Committing the updation made
    print("\nSUCCESS: Successfully updated Product record.\n")
    connection.commit()


# Updating a supplier
def updateSupplier():
    print("UPDATE SUPPLIER:\n")
    print("Press Enter for any attribute you do not wish to update.\n")
    supplier_ID = input("Enter ID of supplier to be updated: ")

    cursor.execute("SELECT * FROM Supplier WHERE Supplier_ID = %s", (supplier_ID,))
    row = cursor.fetchone()
    if row is None:
        print(f"\nUPDATION ERROR: Supplier with ID {supplier_ID} not found.\n")
        return

    company = input("Enter new company name: ")
    if company !=  "": row["Company"] = company
    email = input("Enter new email: ")
    number = input("Enter new number: ")

    # Storing queries
    query_1 = "UPDATE Supplier SET Company = %s WHERE Supplier_ID = %s"
    query_2 = "UPDATE Supplier_email SET Email = %s WHERE Supplier_ID = %s"
    query_3 = "UPDATE Supplier_contact_number SET Supplier_number = %s WHERE Supplier_ID = %s"

    try:
        cursor.execute(query_1, (row["Company"], supplier_ID))

        if email != "":
            cursor.execute(query_2, (email, supplier_ID))
        if number != "":
            cursor.execute(query_3, (number, supplier_ID))

    except Exception as e:
        print(f"\nUPDATION ERROR: Failed to update Supplier record - {e}\n")
        return

    # Committing the updation made
    print("\nSUCCESS: Successfully updated Supplier record.\n")
    connection.commit()


# Updating a shipping company
def updateShippingCompany():
    print("UPDATE SHIPPING COMPANY:\n")
    print("Press Enter for any attribute you do not wish to update.\n")
    shipping_ID = input("Enter ID of shipping company to be updated: ")

    cursor.execute("SELECT * FROM Shipping_company WHERE Company_ID = %s", (shipping_ID,))
    row = cursor.fetchone()
    if row is None:
        print(f"\nUPDATION ERROR: Shipping_company with ID {shipping_ID} not found.\n")
        return

    company = input("Enter new company name: ")
    if company !=  "": row["Company_name"] = company
    email = input("Enter new email: ")
    number = input("Enter new number: ")

    # Storing queries
    query_1 = "UPDATE Shipping_company SET Company_name = %s WHERE Company_ID = %s"
    query_2 = "UPDATE Shipping_company_email SET Email = %s WHERE Shipping_company_ID = %s"
    query_3 = "UPDATE Shipping_company_contact_number SET Phone_number = %s WHERE Shipping_company_ID = %s"

    try:
        cursor.execute(query_1, (row["Company_name"], shipping_ID))

        if email != "":
            cursor.execute(query_2, (email, shipping_ID))
        if number != "":
            cursor.execute(query_3, (number, shipping_ID))

    except Exception as e:
        print(f"\nUPDATION ERROR: Failed to update Shipping Company record - {e}\n")
        return

    # Committing the updation made
    print("\nSUCCESS: Successfully updated Shipping Company record.\n")
    connection.commit()

#-----------------RETRIEVALS-----------------#

# To display all details of products of a particular brand
def displayProductDetails():
    try:
        brand = input("Enter brand: ")
        cursor.execute("SELECT * FROM Product WHERE Brand = %s", (brand,))
        print(tabulate(cursor.fetchall(), headers="keys", tablefmt="psql"))
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")


# To display names of employees with salary greater than a given amount
def displayEmployee():
    try:
        minSalary = input("Enter minimum salary: ")
        cursor.execute("SELECT First_name,Last_name FROM Employee WHERE Salary > %s",(minSalary,))
        print(tabulate(cursor.fetchall(), headers="keys", tablefmt="psql"))
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")


# To display average stars of a given product ID
def averageStars():
    try:
        productID = input("Enter product ID: ")
        cursor.execute("SELECT AVG(Stars) FROM Review WHERE Product_ID = %s", (productID,))
        stars = cursor.fetchone()["AVG(Stars)"]
        if stars is None:
            print(f"\nINSERTION ERROR: Product with ID {productID} not found.\n")
            return

        print(f"Average number of stars: {stars}")
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")


# To search by name for orders shipped by a shipping company
def ordersShippedByCompany():
    try:
        shipperName = input("Enter shipping company name (partial match): ")
        cursor.execute("SELECT * FROM Orders WHERE Shipping_company_ID IN (SELECT Company_ID FROM Shipping_company WHERE Company_name LIKE %s)", (shipperName + '%',))
        print(tabulate(cursor.fetchall(), headers="keys", tablefmt="psql"))
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")


# To display analysis report for average rating of all products supplied by a given Supplier ID
def avgRatingOfSupplier():
    supplier = input("Enter supplier ID: ")
    cursor.execute("SELECT Product_ID FROM Product WHERE Supplier_ID = %s", (supplier,))

    if cursor.fetchone() is None:
        print(f"\nEXECUTION ERROR: Supplier with ID {supplier} not found.\n")
        return

    try: 
        cursor.execute("SELECT COUNT(Product_ID) FROM Review WHERE Product_ID IN (SELECT Product_ID FROM Product WHERE Supplier_ID = %s)", (supplier,))
        starNum = cursor.fetchone()["COUNT(Product_ID)"]
        cursor.execute("SELECT SUM(Stars) FROM Review WHERE Product_ID IN (SELECT Product_ID FROM Product WHERE Supplier_ID = %s)", (supplier,))
        starSum = cursor.fetchone()["SUM(Stars)"]
            
        print(f"Average rating: {starSum/starNum}")
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")


# To display analysis report of number of products of a particular category ordered
def numberOfProductsOfCategoryOrdered():
    try:
        category = input("Enter category: ")
        cursor.execute("SELECT COUNT(Product_ID) FROM Product_purchased WHERE Product_ID IN (SELECT Product_ID FROM Product WHERE Category = %s)", (category,))
        count = cursor.fetchone()["COUNT(Product_ID)"]
        print(f"Number of products: {count}")
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")
    

# To display analysis report of total profit from the orders in the past 3 months
def profitIn3Months():
    try:
        cursor.execute("SELECT SUM(Amount) FROM Payment WHERE Order_ID IN (SELECT Order_ID FROM Orders WHERE Order_date >= DATE_ADD(NOW(), INTERVAL -3 MONTH))")
        netProfit = cursor.fetchone()["SUM(Amount)"]
        print(f"Net profit in last 3 months: {netProfit}")
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")

#-----------------ADDITIONAL FUNCTIONS-----------------#

# To find the number of products listed by a Supplier from the Products table
def numProductsListed():
    supplierID = input("Enter supplier ID: ")
    query = "SELECT COUNT(*) FROM Product WHERE Supplier_ID = %s"

    try:
        cursor.execute(query, (supplierID,))
        value = cursor.fetchone()['COUNT(*)']
        if value is None:
            print(f"\nEXECUTION ERROR: Supplier with ID {supplierID} not found.\n")
            return

        print(f"\nNumber of products listed by supplier with ID {supplierID}: {value}\n")
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")


# To derive the age of a customer from date of birth
def deriveCustomerAge():
    customerID = input("Enter customer ID: ")
    cursor.execute("SELECT * FROM Customer WHERE Customer_ID = %s", (customerID,))
    row = cursor.fetchone()
    if row is None:
        print(f"\nEXECUTION ERROR: Customer with ID {customerID} not found.\n")
        return
    
    try:
        day = row["Day_of_birth"]
        month = row["Month_of_birth"]
        year = row["Year_of_birth"]
    
        cursor.execute("SELECT TIMESTAMPDIFF(YEAR,'%s-%s-%s',CURDATE()) as Age FROM Customer WHERE Customer_ID = %s", (year, month, day, customerID))
        print(f"Age: {cursor.fetchone()['Age']}")
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")


# To derive the age of an employee from date of birth
def deriveEmployeeAge():
    employeeID = input("Enter employee ID: ")
    cursor.execute("SELECT * FROM Employee WHERE Employee_ID = %s", (employeeID,))
    row = cursor.fetchone()
    if row is None:
        print(f"\nEXECUTION ERROR: Employee with ID {employeeID} not found.\n")
        return
    
    try:
        day = row["Day_of_birth"]
        month = row["Month_of_birth"]
        year = row["Year_of_birth"]
    
        cursor.execute("SELECT TIMESTAMPDIFF(YEAR,'%s-%s-%s',CURDATE()) as Age FROM Employee WHERE Employee_ID = %s", (year, month, day, employeeID))
        print(f"Age: {cursor.fetchone()['Age']}")
    except Exception as e:
        print(f"\nEXECUTION ERROR: Failed to execute query - {e}\n")

#-----------------MENU FUNCTIONS-----------------#

# Menu to access insertion queries
def insertFunctions():
    print("\n-----INSERTION FUNCTIONS-----\n")
    print("Choose an operation:\n")
    print("1. Insert Customer")
    print("2. Insert Employee")
    print("3. Insert Product")
    print("4. Insert Order")
    print("5. Insert Supplier")
    print("6. Insert Shipping Company")
    print("7. Insert Review")
    print("8. Return")

    option = int(input("\nEnter option: "))

    if option < 1 or option > 8:
        print("\nERROR: Invalid option entered.\n")
        time.sleep(2)
        return

    sp.call("clear", shell=True)

    if option == 1:
        insertCustomer()
    elif option == 2:
        insertEmployee()
    elif option == 3:
        insertProduct()
    elif option == 4:
        insertOrder()
    elif option == 5:
        insertSupplier()
    elif option == 6:
        insertShippingCompany()
    elif option == 7:
        insertReview()
    elif option == 8:
        return

    time.sleep(2)


# Menu to access deletion queries
def deleteFunctions():
    print("\n-----DELETION FUNCTIONS-----\n")
    print("Choose an operation:\n")
    print("1. Delete Customer")
    print("2. Delete Employee")
    print("3. Delete Product")
    print("4. Delete Order")
    print("5. Delete Supplier")
    print("6. Delete Shipping Company")
    print("7. Delete Review")
    print("8. Return")

    option = int(input("\nEnter option: "))

    if option < 1 or option > 8:
        print("\nERROR: Invalid option entered.\n")
        time.sleep(2)
        return

    sp.call("clear", shell=True)

    if option == 1:
        deleteCustomer()
    elif option == 2:
        deleteEmployee()
    elif option == 3:
        deleteProduct()
    elif option == 4:
        deleteOrder()
    elif option == 5:
        deleteSupplier()
    elif option == 6:
        deleteShippingCompany()
    elif option == 7:
        deleteReview()
    elif option == 8:
        return

    time.sleep(2)


# Menu to access update queries
def updateFunctions():
    print("\n-----UPDATION FUNCTIONS-----\n")
    print("Choose an operation:\n")
    print("1. Update Customer")
    print("2. Update Employee")
    print("3. Update Product")
    print("4. Update Supplier")
    print("5. Update Shipping Company")
    print("6. Return")

    option = int(input("\nEnter option: "))

    if option < 1 or option > 6:
        print("\nERROR: Invalid option entered.\n")
        time.sleep(2)
        return

    sp.call("clear", shell=True)

    if option == 1:
        updateCustomer()
    elif option == 2:
        updateEmployee()
    elif option == 3:
        updateProduct()
    elif option == 4:
        updateSupplier()
    elif option == 5:
        updateShippingCompany()
    elif option == 6:
        return

    time.sleep(2)


# Menu to access data retrieval functions
def dataRetrieval():
    print("\n-----DATA RETRIEVAL FUNCTIONS-----\n")
    print("Choose an operation:\n")
    print("1. Display all details of products of a particular brand")
    print("2. Display the names of employees with salary greater than a certain amount")
    print("3. Diplay the average number of stars for a particular product")
    print("4. Search for orders shipped by a particular shipping company by name")
    print("5. Average rating of all products supplied by a given supplier")
    print("6. Number of products of a particular category ordered")
    print("7. Total profit from orders in the last 3 months")
    print("8. Return")

    option = int(input("\nEnter option: "))

    if option < 1 or option > 8:
        print("\nERROR: Invalid option entered.\n")
        time.sleep(2)
        return

    sp.call("clear", shell=True)

    if option == 1:
        displayProductDetails()
    elif option == 2:
        displayEmployee()
    elif option == 3:
        averageStars()
    elif option == 4:
        ordersShippedByCompany()
    elif option == 5:
        avgRatingOfSupplier()
    elif option == 6:
        numberOfProductsOfCategoryOrdered()
    elif option == 7:
        profitIn3Months()
    elif option == 8:
        return

    time.sleep(2)


# Menu to access additional functions
def additionalFunctions():
    print("\n-----ADDITIONAL FUNCTIONS-----\n")
    print("Choose an operation:\n")
    print("1. Display number of products listed by a particular supplier")
    print("2. Calculate customer age")
    print("3. Calculate employee age")
    print("4. Return")

    option = int(input("\nEnter option: "))

    if option < 1 or option > 4:
        print("\nERROR: Invalid option entered.\n")
        time.sleep(2)
        return

    sp.call("clear", shell=True)

    if option == 1:
        numProductsListed()
    elif option == 2:
        deriveCustomerAge()
    elif option == 3:
        deriveEmployeeAge()
    elif option == 4:
        return

    time.sleep(2)

#-----------------MAIN LOOP-----------------#

while True:
    try:
        sp.call("clear", shell=True)

        # Creating a cursor to execute queries
        with connection.cursor() as cursor:
            print("\n-----eCOMMERCE WEBSITE DATABASE CLI-----\n")
            print("Choose an operation:\n")
            print("1. Insert new record")
            print("2. Delete existing record")
            print("3. Update existing record")
            print("4. Data Retrieval")
            print("5. Additional Functions")
            print("6. Exit")

            option = int(input("\nEnter option: "))

            if option < 1 or option > 6:
                print("\nERROR: Invalid option entered. Please try again.\n")
                time.sleep(2)
                continue

            sp.call("clear", shell=True)

            if option == 1:
                insertFunctions()
            elif option == 2:
                deleteFunctions()
            elif option == 3:
                updateFunctions()
            elif option == 4:
                dataRetrieval()
            elif option == 5:
                additionalFunctions()
            elif option == 6:
                print("\nThank you for using the program!\n")
                break

    except:
        print("\nUNEXPECTED ERRORS: Exiting program.\n")
        break

# Closing the connection
connection.close()
