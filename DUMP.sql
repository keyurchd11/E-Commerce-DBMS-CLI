-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `Customer_ID` int NOT NULL AUTO_INCREMENT,
  `First_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Day_of_birth` int NOT NULL,
  `Month_of_birth` int NOT NULL,
  `Year_of_birth` int NOT NULL,
  `Gender` varchar(15) NOT NULL,
  `Address` varchar(100) NOT NULL,
  PRIMARY KEY (`Customer_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'Arjun','Muraleedharan',21,3,2002,'Male','F:12,Bldg:312,Rd:422,Kerala,India'),(2,'Keyur','Chaudhari',11,6,2002,'Male','F:21,Bldg:123,Rd:792,Gujarat,India'),(3,'Aarush','Jain',4,1,2002,'Male','F:23,Bldg:762,Rd:718,Punjab,India'),(4,'Aryan','Gupta',22,11,2002,'Male','F:6,Bldg:009,Rd:609,Singrauli,Madhya Pradesh,India'),(5,'Srikar','Desu',28,12,2002,'Male','F:12,Bldg:1204,Rd:1602,Bangalore,Karnataka,India'),(6,'Vidit','Jain',27,12,2002,'Male','F:12,Bldg:126,Rd:123,Mumbai,Maharashtra,India'),(7,'Vivek','Mathur',4,12,2002,'Male','12,73,MP,India');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_email`
--

DROP TABLE IF EXISTS `Customer_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_email` (
  `Customer_ID` int NOT NULL,
  `Email` varchar(100) NOT NULL,
  PRIMARY KEY (`Customer_ID`),
  UNIQUE KEY `Email` (`Email`),
  CONSTRAINT `Customer_email_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_email`
--

LOCK TABLES `Customer_email` WRITE;
/*!40000 ALTER TABLE `Customer_email` DISABLE KEYS */;
INSERT INTO `Customer_email` VALUES (3,'aarushj09@gmail.com'),(1,'arjunM@gmail.com'),(4,'cryanGupta@gmail.com'),(6,'fangahawk@gmail.com'),(5,'flyingPenguin_12@gmail.com'),(2,'keyurChaudhari@gmail.com'),(7,'vivek@gmail.com');
/*!40000 ALTER TABLE `Customer_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_phone_number`
--

DROP TABLE IF EXISTS `Customer_phone_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_phone_number` (
  `Customer_ID` int NOT NULL,
  `Number` int NOT NULL,
  PRIMARY KEY (`Customer_ID`),
  UNIQUE KEY `Number` (`Number`),
  CONSTRAINT `Customer_phone_number_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_phone_number`
--

LOCK TABLES `Customer_phone_number` WRITE;
/*!40000 ALTER TABLE `Customer_phone_number` DISABLE KEYS */;
INSERT INTO `Customer_phone_number` VALUES (6,6),(3,32754575),(1,33756875),(7,35728118),(5,35797828),(2,36746876),(4,36916901);
/*!40000 ALTER TABLE `Customer_phone_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Developer`
--

DROP TABLE IF EXISTS `Developer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Developer` (
  `Employee_ID` int NOT NULL,
  `Project_name` varchar(50) NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  CONSTRAINT `Developer_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Developer`
--

LOCK TABLES `Developer` WRITE;
/*!40000 ALTER TABLE `Developer` DISABLE KEYS */;
INSERT INTO `Developer` VALUES (3,'projectProject');
/*!40000 ALTER TABLE `Developer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `Employee_ID` int NOT NULL AUTO_INCREMENT,
  `First_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Day_of_birth` int NOT NULL,
  `Month_of_birth` int NOT NULL,
  `Year_of_birth` int NOT NULL,
  `Gender` varchar(15) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Salary` int NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Designation` varchar(50) NOT NULL,
  `Date_of_joining` date NOT NULL,
  PRIMARY KEY (`Employee_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (1,'Abhilash','Chatterjee',3,12,1992,'Male','12,Sai Darshan Society, Delhi,India',65000,'Sales','Manager','2010-05-12'),(2,'Kishore','Kumar',23,1,1992,'Male','13,Bldg:123,Manama,Bahrain',500000,'IT','Head','2020-07-01'),(3,'Pramod','Bhudramane',12,12,2001,'Male','jadeReaper@yahoo.com',500000,'Developer','Head','2020-03-12');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_email`
--

DROP TABLE IF EXISTS `Employee_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_email` (
  `Employee_ID` int NOT NULL,
  `Email` varchar(100) NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  UNIQUE KEY `Email` (`Email`),
  CONSTRAINT `Employee_email_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_email`
--

LOCK TABLES `Employee_email` WRITE;
/*!40000 ALTER TABLE `Employee_email` DISABLE KEYS */;
INSERT INTO `Employee_email` VALUES (1,'abhi@gmail.com'),(2,'akcube@gmail.com'),(3,'jadeReaper@yahoo.com');
/*!40000 ALTER TABLE `Employee_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_phone_number`
--

DROP TABLE IF EXISTS `Employee_phone_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_phone_number` (
  `Employee_ID` int NOT NULL,
  `Number` int NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  UNIQUE KEY `Number` (`Number`),
  CONSTRAINT `Employee_phone_number_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_phone_number`
--

LOCK TABLES `Employee_phone_number` WRITE;
/*!40000 ALTER TABLE `Employee_phone_number` DISABLE KEYS */;
INSERT INTO `Employee_phone_number` VALUES (2,3672912),(1,3681963),(3,36281812);
/*!40000 ALTER TABLE `Employee_phone_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Items_bought`
--

DROP TABLE IF EXISTS `Items_bought`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Items_bought` (
  `Order_ID` int NOT NULL,
  `Product_ID` int NOT NULL,
  `Quantity` int NOT NULL,
  KEY `Order_ID` (`Order_ID`),
  KEY `Product_ID` (`Product_ID`),
  CONSTRAINT `Items_bought_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `Orders` (`Order_ID`) ON DELETE CASCADE,
  CONSTRAINT `Items_bought_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`Product_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Items_bought`
--

LOCK TABLES `Items_bought` WRITE;
/*!40000 ALTER TABLE `Items_bought` DISABLE KEYS */;
INSERT INTO `Items_bought` VALUES (1,1,1),(1,2,1),(1,3,1);
/*!40000 ALTER TABLE `Items_bought` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `Order_ID` int NOT NULL AUTO_INCREMENT,
  `Order_date` date NOT NULL,
  `Shipping_company_ID` int NOT NULL,
  PRIMARY KEY (`Order_ID`),
  KEY `Shipping_company_ID` (`Shipping_company_ID`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`Shipping_company_ID`) REFERENCES `Shipping_company` (`Company_ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES (1,'2020-04-24',1);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Payment`
--

DROP TABLE IF EXISTS `Payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Payment` (
  `Order_ID` int NOT NULL,
  `Amount` int NOT NULL,
  `Mode_of_payment` varchar(20) NOT NULL,
  `Discount_Percentage` int NOT NULL,
  KEY `Order_ID` (`Order_ID`),
  CHECK (`Discount_Percentage` >= 0 AND `Discount_Percentage` <= 100),
  CONSTRAINT `Payment_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `Orders` (`Order_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Payment`
--

LOCK TABLES `Payment` WRITE;
/*!40000 ALTER TABLE `Payment` DISABLE KEYS */;
INSERT INTO `Payment` VALUES (1,60000,'Credit Card',5);
/*!40000 ALTER TABLE `Payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product` (
  `Product_ID` int NOT NULL AUTO_INCREMENT,
  `Category` varchar(50) NOT NULL,
  `Brand` varchar(50) NOT NULL,
  `Model` varchar(50) NOT NULL,
  `Supplier_ID` int NOT NULL,
  `MRP` int NOT NULL,
  `Buying_price` int NOT NULL,
  `Selling_price` int NOT NULL,
  `Available_quantity` int NOT NULL,
  `In_stock` tinyint(1) NOT NULL,
  PRIMARY KEY (`Product_ID`),
  KEY `Supplier_ID` (`Supplier_ID`),
  CONSTRAINT `Product_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (1,'Books','Cengage','MathForJee',1,1000,800,950,119,1),(2,'Laptop','Acer','Helios',2,50000,49000,50000,9,1),(3,'Refrigerator','LG','SmartSaver',3,12000,10000,11999,9,1),(4,'Snacks','Maggi','Maggi Masala Magic',2,20,19,20,1000,1),(5,'Snacks','OreoShake','theOneOnCampus',1,25,20,25,100,1);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product_purchased`
--

DROP TABLE IF EXISTS `Product_purchased`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product_purchased` (
  `Product_ID` int NOT NULL,
  `Customer_ID` int NOT NULL,
  `Order_ID` int NOT NULL,
  `Supplier_ID` int NOT NULL,
  KEY `Product_ID` (`Product_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `Order_ID` (`Order_ID`),
  KEY `Supplier_ID` (`Supplier_ID`),
  CONSTRAINT `Product_purchased_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`Product_ID`) ON DELETE CASCADE,
  CONSTRAINT `Product_purchased_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE,
  CONSTRAINT `Product_purchased_ibfk_3` FOREIGN KEY (`Order_ID`) REFERENCES `Orders` (`Order_ID`) ON DELETE CASCADE,
  CONSTRAINT `Product_purchased_ibfk_4` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product_purchased`
--

LOCK TABLES `Product_purchased` WRITE;
/*!40000 ALTER TABLE `Product_purchased` DISABLE KEYS */;
INSERT INTO `Product_purchased` VALUES (1,2,1,1),(2,2,1,2),(3,2,1,3);
/*!40000 ALTER TABLE `Product_purchased` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Review` (
  `Product_ID` int NOT NULL,
  `Customer_ID` int NOT NULL,
  `Stars` int NOT NULL,
  `Content` text,
  KEY `Product_ID` (`Product_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  CONSTRAINT `Review_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`Product_ID`) ON DELETE CASCADE,
  CONSTRAINT `Review_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Review`
--

LOCK TABLES `Review` WRITE;
/*!40000 ALTER TABLE `Review` DISABLE KEYS */;
INSERT INTO `Review` VALUES (1,2,5,'Extremely Satisfied. Shipped in time. Good quality.'),(3,2,2,'Extremely bad. Not as described.');
/*!40000 ALTER TABLE `Review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shipping_company`
--

DROP TABLE IF EXISTS `Shipping_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shipping_company` (
  `Company_ID` int NOT NULL AUTO_INCREMENT,
  `Company_name` varchar(100) NOT NULL,
  PRIMARY KEY (`Company_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shipping_company`
--

LOCK TABLES `Shipping_company` WRITE;
/*!40000 ALTER TABLE `Shipping_company` DISABLE KEYS */;
INSERT INTO `Shipping_company` VALUES (1,'DLH'),(2,'MoversAndShippers'),(3,'BlueDart');
/*!40000 ALTER TABLE `Shipping_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shipping_company_contact_number`
--

DROP TABLE IF EXISTS `Shipping_company_contact_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shipping_company_contact_number` (
  `Shipping_company_ID` int NOT NULL,
  `Phone_number` int NOT NULL,
  UNIQUE KEY `Phone_number` (`Phone_number`),
  KEY `Shipping_company_ID` (`Shipping_company_ID`),
  CONSTRAINT `Shipping_company_contact_number_ibfk_1` FOREIGN KEY (`Shipping_company_ID`) REFERENCES `Shipping_company` (`Company_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shipping_company_contact_number`
--

LOCK TABLES `Shipping_company_contact_number` WRITE;
/*!40000 ALTER TABLE `Shipping_company_contact_number` DISABLE KEYS */;
INSERT INTO `Shipping_company_contact_number` VALUES (1,12345),(1,36283),(1,73527),(2,62571),(2,78291),(2,98273),(3,123420),(3,8273517),(3,96237114);
/*!40000 ALTER TABLE `Shipping_company_contact_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shipping_company_email`
--

DROP TABLE IF EXISTS `Shipping_company_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shipping_company_email` (
  `Shipping_company_ID` int NOT NULL,
  `Email` varchar(100) NOT NULL,
  PRIMARY KEY (`Shipping_company_ID`),
  UNIQUE KEY `Email` (`Email`),
  CONSTRAINT `Shipping_company_email_ibfk_1` FOREIGN KEY (`Shipping_company_ID`) REFERENCES `Shipping_company` (`Company_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shipping_company_email`
--

LOCK TABLES `Shipping_company_email` WRITE;
/*!40000 ALTER TABLE `Shipping_company_email` DISABLE KEYS */;
INSERT INTO `Shipping_company_email` VALUES (3,'blue@dart.com'),(1,'dlh@dlhtech.in'),(2,'move@ship.com');
/*!40000 ALTER TABLE `Shipping_company_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier`
--

DROP TABLE IF EXISTS `Supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier` (
  `Supplier_ID` int NOT NULL AUTO_INCREMENT,
  `Company` varchar(100) NOT NULL,
  PRIMARY KEY (`Supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier`
--

LOCK TABLES `Supplier` WRITE;
/*!40000 ALTER TABLE `Supplier` DISABLE KEYS */;
INSERT INTO `Supplier` VALUES (1,'Tata'),(2,'Reliance'),(3,'SupplierSupplier'),(4,'ALBA');
/*!40000 ALTER TABLE `Supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier_contact_number`
--

DROP TABLE IF EXISTS `Supplier_contact_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier_contact_number` (
  `Supplier_ID` int NOT NULL,
  `Supplier_number` int NOT NULL,
  UNIQUE KEY `Supplier_ID` (`Supplier_ID`),
  UNIQUE KEY `Supplier_number` (`Supplier_number`),
  CONSTRAINT `Supplier_contact_number_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier_contact_number`
--

LOCK TABLES `Supplier_contact_number` WRITE;
/*!40000 ALTER TABLE `Supplier_contact_number` DISABLE KEYS */;
INSERT INTO `Supplier_contact_number` VALUES (1,25738271),(4,35628373),(3,82637137),(2,92372828);
/*!40000 ALTER TABLE `Supplier_contact_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier_email`
--

DROP TABLE IF EXISTS `Supplier_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier_email` (
  `Supplier_ID` int NOT NULL,
  `Email` varchar(100) NOT NULL,
  UNIQUE KEY `Supplier_ID` (`Supplier_ID`),
  UNIQUE KEY `Email` (`Email`),
  CONSTRAINT `Supplier_email_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier_email`
--

LOCK TABLES `Supplier_email` WRITE;
/*!40000 ALTER TABLE `Supplier_email` DISABLE KEYS */;
INSERT INTO `Supplier_email` VALUES (4,'alba@aluminium.com'),(2,'reliance@rel.in'),(3,'supplier@supplier.com'),(1,'tata@tata.com');
/*!40000 ALTER TABLE `Supplier_email` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26 20:51:30
