-- Customer

CREATE TABLE Customer(
	Customer_ID INTEGER NOT NULL AUTO_INCREMENT, 
    First_name VARCHAR(20) NOT NULL, 
    Last_name VARCHAR(20) NOT NULL,
    Day_of_birth INTEGER NOT NULL, 
    Month_of_birth INTEGER NOT NULL, 
    Year_of_birth INTEGER NOT NULL, 
    Gender VARCHAR(15) NOT NULL, 
    Address VARCHAR(100) NOT NULL,
    PRIMARY KEY(Customer_ID)
);

CREATE TABLE Customer_email(
	Customer_ID INTEGER NOT NULL, 
    Email VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(Customer_ID),
    FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID) ON DELETE CASCADE
);

CREATE TABLE Customer_phone_number(
	Customer_ID INTEGER NOT NULL, 
    Number INTEGER NOT NULL UNIQUE,
    PRIMARY KEY(Customer_ID),
    FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID) ON DELETE CASCADE
);

-- Employee

CREATE TABLE Employee(
	Employee_ID INTEGER NOT NULL AUTO_INCREMENT,
    First_name VARCHAR(20) NOT NULL, 
    Last_name VARCHAR(20) NOT NULL, 
    Day_of_birth INTEGER NOT NULL, 
    Month_of_birth INTEGER NOT NULL, 
    Year_of_birth INTEGER NOT NULL, 
    Gender VARCHAR(15) NOT NULL, 
    Address VARCHAR(100) NOT NULL,
    Salary INTEGER NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Designation VARCHAR(50) NOT NULL,
    Date_of_joining DATE NOT NULL,
    PRIMARY KEY(Employee_ID)
);

CREATE TABLE Employee_phone_number(
	Employee_ID INTEGER NOT NULL,
    Number INTEGER UNIQUE NOT NULL UNIQUE,
    PRIMARY KEY(Employee_ID),
    FOREIGN KEY(Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE
);

CREATE TABLE Employee_email(
	Employee_ID INTEGER NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(Employee_ID),
    FOREIGN KEY(Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE
);

-- Product

CREATE TABLE Product(
	Product_ID INTEGER NOT NULL AUTO_INCREMENT,
    Category VARCHAR(50) NOT NULL,
    Brand VARCHAR(50) NOT NULL,
    Model VARCHAR(50) NOT NULL,
    MRP INTEGER NOT NULL,
    Buying_price INTEGER NOT NULL,
    Selling_price INTEGER NOT NULL,
    Available_quantity INTEGER NOT NULL,
    In_stock BOOL NOT NULL,
    PRIMARY KEY(Product_ID)
);

-- Shipping Company

CREATE TABLE Shipping_company(
	Company_ID INTEGER NOT NULL AUTO_INCREMENT,
    Company_name VARCHAR(100) NOT NULL,
    PRIMARY KEY(Company_ID)
);

CREATE TABLE Shipping_company_contact_number(
	Shipping_company_ID INTEGER NOT NULL,
    Phone_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(Shipping_company_ID) REFERENCES Shipping_company(Company_ID)
);

CREATE TABLE Shipping_company_email(
	Shipping_company_ID INTEGER NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(Shipping_company_ID),
    FOREIGN KEY(Shipping_company_ID) REFERENCES Shipping_company(Company_ID)
);

-- Order (Renamed to Orders to prevent clash with keyword)

CREATE TABLE Orders(
	Order_ID INTEGER NOT NULL AUTO_INCREMENT,
    Order_date DATE NOT NULL,
    Shipping_company_ID INTEGER NOT NULL,
    PRIMARY KEY(Order_ID),
    FOREIGN KEY(Shipping_company_ID) REFERENCES Shipping_company(Company_ID) ON DELETE CASCADE
);

-- Developer

CREATE TABLE Developer(
	Employee_ID INTEGER NOT NULL,
    Project_name VARCHAR(50) NOT NULL,
    PRIMARY KEY(Employee_ID),
    FOREIGN KEY(Employee_ID) REFERENCES Employee(Employee_ID) ON DELETE CASCADE
);

-- Supplier

CREATE TABLE Supplier(
	Supplier_ID INTEGER NOT NULL AUTO_INCREMENT,
    Company VARCHAR(100) NOT NULL,
    PRIMARY KEY(Supplier_ID)
);

CREATE TABLE Supplier_contact_number(
	Supplier_ID INTEGER NOT NULL UNIQUE,
    Supplier_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(Supplier_ID) REFERENCES Supplier(Supplier_ID)
);

CREATE TABLE Supplier_email(
	Supplier_ID INTEGER NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    FOREIGN KEY(Supplier_ID) REFERENCES Supplier(Supplier_ID)
);

-- Review

CREATE TABLE Review(
	Product_ID INTEGER NOT NULL,
    Customer_ID INTEGER NOT NULL,
    Stars INTEGER NOT NULL,
    Content TEXT,
    FOREIGN KEY(Product_ID) REFERENCES Product(Product_ID),
    FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID)
);

-- Items Bought

CREATE TABLE Items_bought(
    Order_ID INTEGER NOT NULL,
    Product_ID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    FOREIGN KEY(Order_ID) REFERENCES Orders(Order_ID),
    FOREIGN KEY(Product_ID) REFERENCES Product(Product_ID)
);

-- Payment

CREATE TABLE Payment(
    Order_ID INTEGER NOT NULL,
    Amount INTEGER NOT NULL,
    Mode_of_payment VARCHAR(20) NOT NULL,
    Discount_Percentage INTEGER NOT NULL,
    FOREIGN KEY(Order_ID) REFERENCES Orders(Order_ID)
);

-- Product Purchased

CREATE TABLE Product_purchased(
	Product_ID INTEGER NOT NULL,
    Customer_ID INTEGER NOT NULL,
    Order_ID INTEGER NOT NULL,
    Supplier_ID INTEGER NOT NULL,
    FOREIGN KEY(Product_ID) REFERENCES Product(Product_ID),
    FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY(Order_ID) REFERENCES Orders(Order_ID),
    FOREIGN KEY(Supplier_ID) REFERENCES Supplier(Supplier_ID)
);
