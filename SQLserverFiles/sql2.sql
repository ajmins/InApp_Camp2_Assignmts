--AJMI N S
--QUESTION 2


--OrderDetails Table
--+---------+------------+------------+---------------+----------------+
-- | OrderId | OrderDate | OrderPrice | OrderQuantity | CustomerName |
-- +---------+------------+------------+---------------+---------------+
-- | 1 | 2020-12-22 | 270 | 2 | Jayesh |
-- | 2 | 2019-08-10 | 280 | 4 | Abhilash |
-- | 3 | 2019-07-13 | 600 | 5 | Lily |
-- | 4 | 2020-07-15 | 520 | 1 | Jayesh |
-- | 5 | 2020-12-22 | 1200 | 4 | Aswathy |
-- | 6 | 2019-10-02 | 720 | 3 | Jayesh |
-- | 7 | 2020-11-03 | 3000 | 2 | Lily |
-- | 8 | 2020-12-22 | 1100 | 4 | Aswathy |
-- | 9 | 2019-12-29 | 5500 | 2 | Jayesh |
-- +---------+------------+------------+---------------+---------------+
--ProductDetails Table
-- +------------+---------+------------------+----------------+-----------+
-- | Product_id | OrderId | Manufacture_Date | Product_Name | Manufr_id |
-- +------------+---------+------------------+----------------+-----------+
-- | 145 | 2 | 2019-12-23 | MobilePhone | 1 |
-- | 147 | 6 | 2019-08-15 | MobilePhone | 3 |
-- | 435 | 5 | 2018-11-04 | MobilePhone | 1 |
-- | 783 | 1 | 2017-11-03 | LED TV | 2 |
-- | 784 | 4 | 2019-11-28 | LED TV | 2 |
-- | 123 | 2 | 2019-10-03 | Laptop | 2 |
-- | 267 | 5 | 2019-21-03 | Headphone | 4 |
-- | 333 | 9 | 2017-12-12 | Laptop | 1 |
-- | 344 | 3 | 2018-11-03 | Laptop | 1 |
-- | 233 | 3 | 2019-11-30 | PowerBank | 2 |
-- | 567 | 6 | 2019-09-03 | PowerBank | 2 |
-- +------------+---------+------------------+----------------+-----------+
--ManufacturerDetails Table
-- +-----------+-------------+
-- | Manufr_id | Manufr_name |
-- +-----------+-------------+
-- | 1 | Samsung |
-- | 2 | Sony |
-- | 3 | Mi |
-- | 4 | Boat |
-- +-----------+-------------+--Normalize
------------
--The database into its 3rd Normal form. Create necessary sub-tables

USE employee_db1;

CREATE TABLE CustomerDetails(
	CustID INT PRIMARY KEY,
	CustomerName VARCHAR(50)
);

CREATE TABLE ProductNameDetails(
	ProductNo INT PRIMARY KEY,
	Product_Name VARCHAR(50)
);

CREATE TABLE ManufacturerDetails(
	Manufr_id INT PRIMARY KEY,
	Manufr_name VARCHAR(50)
);

CREATE TABLE OrderDetails(
	OrderId INT PRIMARY KEY,
	OrderDate DATE,
	OrderPrice INT,
	OrderQuantity SMALLINT,
	CustID INT FOREIGN KEY REFERENCES CustomerDetails(CustID),
);

CREATE TABLE ProductDetails(
	Product_id INT PRIMARY KEY,
	OrderId INT FOREIGN KEY REFERENCES OrderDetails(OrderId),
	Mnufacture_Date DATE,
	ProductNo INT FOREIGN KEY REFERENCES ProductNameDetails(ProductNo),
	Manufr_id INT FOREIGN KEY REFERENCES ManufacturerDetails(Manufr_id),
);


INSERT INTO ManufacturerDetails VALUES
(1,'Samsung'),
(2,'Sony'),
(3, 'Mi'),
(4,'Boat');

INSERT INTO CustomerDetails VALUES
(01,'Jayesh'),
(02,'Abhilash'),
(03,'Lily'),
(04,'Aswathy');

INSERT INTO ProductNameDetails VALUES
(001,'MobilePhone'),
(002, 'LED TV'),
(003, 'Laptop'),
(004, 'Headphone'),
(005, 'PowerBank');

INSERT INTO ProductDetails VALUES
(145, 2, '2019-12-23', 001, 1),
(147, 6, '2019-08-15', 001, 3),
(435, 5, '2018-11-04', 001, 1),
(783, 1, '2017-11-03', 002, 2),
(784, 4, '2019-11-28', 002, 2),
(123, 2, '2019-10-03', 003, 2),
(267, 5, '2019-03-21', 004, 4),
(333, 9, '2017-12-12', 003, 1),
(344, 3, '2018-11-03', 003, 1),
(233, 3, '2019-11-30', 005, 2),
(567, 6, '2019-09-03', 005, 2);

INSERT INTO OrderDetails VALUES
(1, '2020-12-22', 270, 2, 1),
(2, '2019-08-10', 280, 4, 2),
(3, '2019-07-13', 600, 5, 3),
(4, '2020-07-15', 520, 1, 1),
(5, '2020-12-22', 1200, 4, 4),
(6, '2019-10-02', 720, 3, 1),
(7, '2020-11-03', 3000, 2, 3),
(8, '2020-12-22', 1100, 4, 4),
(9, '2019-12-29', 5500, 2, 1);


--view values
SELECT * FROM OrderDetails;
SELECT * FROM ProductDetails;
SELECT * FROM ManufacturerDetails;
SELECT * FROM ProductNameDetails;
SELECT * FROM CustomerDetails;

---------------------------------------------------------------------
--QUERIES--
----------------------------------------------------------------------

--1) Total number of orders placed in each year.

SELECT COUNT( OrderId)AS 'OrderCount',YEAR(OrderDate) AS 'Year'
	FROM OrderDetails
	GROUP BY YEAR(OrderDate)
				--OrderCount	Year
				--4				2019
				--5				2020

--2) Total number of orders placed in each year by Jayesh.
SELECT COUNT(OrderId) AS 'OrderCount',YEAR(OrderDate) AS 'Year', CustomerName
	FROM OrderDetails
	JOIN CustomerDetails ON OrderDetails.CustID = CustomerDetails.CustID
	WHERE CustomerName LIKE 'Jayesh'
			--	GROUP BY YEAR(OrderDate), CustomerName;
			--	OrderCount	Year	CustomerName
			--2	2019	Jayesh
			--2	2020	Jayesh


--3) Products which are ordered in the same year of its manufacturing year.
SELECT Product_id, Product_Name, YEAR(OrderDate) AS 'Year'
	FROM OrderDetails
	JOIN ProductDetails ON ProductDetails.OrderId = OrderDetails.OrderId
	JOIN ProductNameDetails ON ProductNameDetails.ProductNo = ProductDetails.ProductNo
	WHERE YEAR(OrderDate) = YEAR(Mnufacture_Date);
				--Product_id	Product_Name	Year
				--123	Laptop	2019
				--145	MobilePhone	2019
				--147	MobilePhone	2019
				--233	PowerBank	2019
				--567	PowerBank	2019

--4) Products which is ordered in the same year of its manufacturing year where the Manufacturer is ‘Samsung’.
SELECT DISTINCT Product_Name, YEAR(OrderDate) AS 'Year'
	FROM OrderDetails
	JOIN ProductDetails ON ProductDetails.OrderId = OrderDetails.OrderId
	JOIN ProductNameDetails ON ProductNameDetails.ProductNo = ProductDetails.ProductNo
	JOIN ManufacturerDetails ON ManufacturerDetails.Manufr_id = ProductDetails.Manufr_id
	WHERE YEAR(OrderDate) = YEAR(Mnufacture_Date ) AND Manufr_name = 'Samsung';

			--Product_Name	Year
			--MobilePhone	2019

--5) Total number of products ordered every year.
SELECT SUM( OrderQuantity)AS 'OrderCount',YEAR(OrderDate) AS 'Year'
	FROM OrderDetails
	GROUP BY YEAR(OrderDate)
					--OrderCount	Year
					--14	2019
					--13	2020

--6) Display the total number of products ordered every year made by sony.
SELECT SUM( OrderQuantity)AS 'OrderCount',YEAR(OrderDate) AS 'Year'
	FROM OrderDetails
	JOIN ProductDetails ON ProductDetails.OrderId = OrderDetails.OrderId
	JOIN ManufacturerDetails ON ManufacturerDetails.Manufr_id = ProductDetails.Manufr_id
	JOIN ProductNameDetails ON ProductNameDetails.ProductNo = ProductDetails.ProductNo
	WHERE Manufr_name LIKE 'Sony' 
	GROUP BY YEAR(OrderDate);
				--	OrderCount	Year
				--3	2019
				--2	2020

--7) All customers who are ordering mobile phone by samsung.
SELECT CustomerName, OrderDate, Manufr_name
FROM CustomerDetails
JOIN OrderDetails ON OrderDetails.CustID = CustomerDetails.CustID
JOIN ProductDetails ON ProductDetails.OrderId = OrderDetails.OrderId
JOIN ManufacturerDetails ON ManufacturerDetails.Manufr_id = ProductDetails.Manufr_id
JOIN ProductNameDetails ON ProductNameDetails.ProductNo = ProductDetails.ProductNo
WHERE Manufr_name LIKE 'Samsung' AND Product_Name LIKE 'MobilePhone'
				--CustomerName	OrderDate	Manufr_name
				--Abhilash	2019-08-10	Samsung
				--Aswathy	2020-12-22	Samsung

--8) Total number of orders got by each Manufacturer every year.

SELECT COUNT(OrderDetails.OrderId) AS 'OrderCount', Year(OrderDate) AS Year, Manufr_name 
	FROM OrderDetails 
	JOIN ProductDetails ON ProductDetails.OrderId = OrderDetails.OrderId
	JOIN ManufacturerDetails ON ManufacturerDetails.Manufr_id = ProductDetails.Manufr_id
	GROUP BY Manufr_name, Year(OrderDate)
				--	OrderCount	Year	Manufr_name
				--1	2019	Mi
				--3	2019	Samsung
				--3	2019	Sony
				--1	2020	Boat
				--1	2020	Samsung
				--2	2020	Sony

--9) All Manufacturers whose products were sold more than 1500 Rs every year.SELECT SUM(OrderPrice) AS 'Total Price', Manufr_name 
FROM OrderDetails 
JOIN ProductDetails ON ProductDetails.OrderId = OrderDetails.OrderId 
JOIN ManufacturerDetails ON ManufacturerDetails.Manufr_id = ProductDetails.Manufr_id
GROUP BY Manufr_name   HAVING SUM(OrderPrice)>1500			--Total Price	Manufr_name
			--7580	Samsung
			--2390	Sony