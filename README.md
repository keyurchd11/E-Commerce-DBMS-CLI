# eCommerce-DBMS-CLI

This is a CLI for an eCommerce DBMS. Users can interact with it to insert, delete and update data in the database, and view the results of certain predefined functions that provide insight into the services of the eCommerce company.

## Team Members

1. <a href="https://github.com/Aarushj09">Aarush Jain</a>
2. <a href="https://github.com/keyurchd11">Keyur Chaudhari</a>
3. <a href="https://github.com/coniferousdyer">Arjun Muraleedharan</a>

## Setup

1. You must have MySQL Server installed. To do so,
```bash
sudo apt-get update
sudo apt-get install mysql-server
```
When installing the MySQL server for the first time, you will be prompted for a root password with which you can later log in. If for some reason, you aren't asked for the password during installation, try prepending the start command with `sudo` and provide your root password. You can then set a root password or create a new user. 

To start MySQL, run
```bash
mysql -u <user_name> -p
```
You will then be prompted for the user's password.

If you wish to create a new user,
```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
To grant access and modification privileges to this new user, run
```sql
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
```

2. Create a new database for the eCommerce website, using the following SQL command, and then set it up.
```sql
CREATE DATABASE <database_name>;
USE <database_name>;
```

3. To initialise the database with the tables required, run 
```bash
source CREATE_TABLES.sql
```

4. Now, create a `.env` file in the project directory, and paste the following in it. Replace the "xxx"s with the appropriate details for the fields.
```
MYSQL_HOST="localhost"
MYSQL_USER="xxx"
MYSQL_PASSWORD="xxx"
MYSQL_DATABASE="xxx"
``` 

5. You will need to install the required modules to run the CLI. Optionally, you can choose to create a virtual environment for this purpose.
```bash
python3 -m venv <venv_name>
source <venv_name>/bin/activate
```

6. Install the required modules within your virtual environment.
```bash
pip install -r requirements.txt
```

7. Everything is now set up. To run the CLI,
```bash
python3 main.py
```

<b>Note: </b>To exit the virtual environment,
```bash
deactivate
```

## Functions

### Insertion Functions

1. `insertCustomer()`: Insert a customer into the database.

2. `insertEmployee()`: Insert an employee into the database.

3. `insertProduct()`: Insert a product into the database.

4. `insertOrder()`: Insert an order into the database.

5. `insertSupplier()`: Insert a supplier into the database.

6. `insertShippingCompany()`: Insert a database into the database.

7. `insertReview()`: Insert a review into the database.

### Deletion Functions

1. `deleteCustomer()`: Delete a customer from the database.

2. `deleteProduct()`: Delete a product from the database.

3. `deleteSupplier()`: Delete a supplier from the database.

4. `deleteShippingCompany()`: Delete a shipping company from the database.

5. `deleteOrder()`: Delete an order from the database.

6. `deleteReview()`: Delete a review from the database.

7. `deleteEmployee()`: Delete an employee from the database.

### Updation Functions

1. `updateCustomer()`: Update a customer's details in the database.

2. `updateEmployee()`: Update an employee's details in the database.

3. `updateProduct()`: Update a product's details in the database.

4. `updateSupplier()`: Update a supplier's details in the database.

5. `updateShippingCompany()`: Update a shipping company's details in the database.

### Data Retrieval Functions

1. `displayProductDetails()`: Display all details of products of a particular brand.

2. `displayEmployee()`: Display the names of employees with salary greater than a
certain amount.

3. `averageStars()`: Displays the average number of stars for a particular product ID.

4. `ordersShippedByCompany()`: Search (partial text match) for orders shipped by a shipping
company, by name.

5. `avgRatingOfSupplier()`: Analysis report of average rating of all products supplied by a given supplier.

6. `numberOfProductsOfCategoryOrdered()`: Analysis report of number of products of a particular category ordered.

7. `profitIn3Months()`: Analysis report of total profit from the orders in the past 3 months.

### Additional Functions

1. `NumProductsListed()`: To find the number of products listed by a supplier from the Products table.

2. `deriveCustomerAge()`: To derive the age from the date of birth of the customer.

3. `deriveEmployeeAge()`: To derive the age from the date of birth of the employee.

<hr>
<em>This project was developed as part of the Data and Applications course, IIIT Hyderabad.</em>