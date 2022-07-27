--7th July 2022
USE Northwind
SELECT * FROM Customers

--to get the list of tables in the seelcted database
SELECT * FROM Sys.tables

--Aggregate function
SELECT * FROM Products
--MIN
SELECT MIN(UnitPrice) FROM Products
--2.50
--to get a name for the column
SELECT MIN(UnitPrice) AS 'Min Product Price' FROM Products

--MAX
SELECT MAX(UnitPrice) AS 'Max Product Price' FROM Products

--using Aggregate function as a subquery
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE 
UnitPrice = (SELECT MIN(UnitPrice) FROM Products)
--33	Geitost	2.50

--using Aggregate function as a subquery
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE 
UnitPrice = (SELECT MAX(UnitPrice) AS 'Maximum of Product Price' FROM Products)
--38	Côte de Blaye	263.50

--using Aggregate function as a subquery
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE 
UnitPrice = (SELECT AVG(UnitPrice) AS 'Avg Product Price' FROM Products)
-- this won't work becz we cannot put that single unitprice becz we can have same uniprices too

SELECT AVG(UnitPrice) AS 'Avg Product Price' FROM Products
--28.8663

--using Aggregate function as a subquery AVG works in this way
--finding all products greater than avg price value
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE 
UnitPrice > (SELECT AVG(UnitPrice) AS 'Avg Product Price' FROM Products)

SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE 
UnitPrice < (SELECT AVG(UnitPrice) AS 'Avg Product Price' FROM Products)


SELECT * FROM Products

--SUM
SELECT SUM(UnitsInStock) AS 'Total Stock'
FROM Products

SELECT SUM(UnitsInStock) AS 'Total Stock'
FROM Products
WHERE Discontinued = 1

SELECT SUM(UnitsInStock) AS 'Total Stock'
FROM Products
WHERE Discontinued = 0

--cOUNT FUNCTION
SELECT COUNT(ProductID) AS 'Products Count'
FROM Products 

SELECT COUNT(ProductID) AS 'No of Discontinued Products'
FROM Products 
WHERE Discontinued = 1


-- Create a new table
CREATE TABLE cust(
	cust_id INT IDENTITY PRIMARY KEY,
	cust_name VARCHAR(50),
	city VARCHAR(50),
	grade INT,
	sales_amount INT
);

INSERT INTO cust (cust_name,city,grade,sales_amount)
VALUES('Anna','NY',100, 5001),
('Sam','NY',200, 4001),
('Jacob','California',200, 2002),
('Soph','London',300, 6002),
('Joe','paris',300, 9000);

--to fetch the data from the table
SELECT * FROM cust

SELECT COUNT(cust_id) AS 'Total Number of Customers'
FROM cust
--5

--highest and lowest graded customers
SELECT MIN(grade) FROM cust
--100
SELECT MAX(grade) FROM cust
--300

--highest graded customers
SELECT cust_name
FROM cust
WHERE grade = (SELECT MAX(grade) AS 'Highest graded customer' FROM cust)
--Soph
--Joe

--lowest graded customers
SELECT cust_name
FROM cust
WHERE grade = (SELECT MIN(grade) AS 'Lowest graded customer' FROM cust)
--Anna

--average sales amount
SELECT AVG(sales_amount) AS 'Average Sales Amount' FROM cust
--5201

--total sales amount
SELECT SUM(sales_amount) AS 'Total Sales Amount' FROM cust
--26006

USE Northwind

--CLAUSES in SQL
--DISTINCT CLAUSE
SELECT City FROM Customers
SELECT DISTINCT City FROM Customers

SELECT DISTINCT City, Region FROM Customers
--if not present then automatically filed with null values

SELECT DISTINCT City, Region FROM Customers
WHERE Country = 'UK'

SELECT CustomerID, Country FROM Customers

--GROUP BY Clause
SELECT COUNT(CustomerID) AS 'No of Customers', Country
FROM Customers
GROUP BY Country;
--No of Customers	Country
--3	Argentina
--2	Austria
--2	Belgium
--9	Brazil
--3	Canada
--2	Denmark
--2	Finland
--11	France
--11	Germany
--1	Ireland
--3	Italy
--5	Mexico
--1	Norway
--1	Poland
--2	Portugal
--5	Spain
--2	Sweden
--2	Switzerland
--7	UK
--13	USA
--4	Venezuela

SELECT COUNT(CustomerID) AS 'No of Customers', Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID)
--No of Customers	Country
--1	Norway
--1	Poland
--1	Ireland
--2	Portugal
--2	Sweden
--2	Switzerland
--2	Austria
--2	Belgium
--2	Denmark
--2	Finland
--3	Argentina
--3	Canada
--3	Italy
--4	Venezuela
--5	Mexico
--5	Spain
--7	UK
--9	Brazil
--11	France
--11	Germany
--13	USA

--8th July 2022
--WHERE clause 
--WHERE with == and BETWEEN
SELECT CompanyName, city, Country
	FROM Suppliers
	WHERE Country = 'USA'
	ORDER BY CompanyName

SELECT * FROM Employees
	WHERE EmployeeID BETWEEN 1 AND 5

--WHERE with IN and LIKE
SELECT * FROM Employees
	WHERE EmployeeID IN(1,2,3)

SELECT * FROM Employees
	WHERE FirstName LIKE 'Robert' 

--ORDER BY Clause
--IF ascending order no need to specify it explicitly, for descending need to specify it explicitly
SELECT FirstName, BirthDate 
	FROM Employees
	ORDER BY BirthDate DESC;

SELECT FirstName, BirthDate 
	FROM Employees
	ORDER BY BirthDate DESC, FirstName ASC;

--HAVING Clause
--We cannot use WHERE clause with aggregate function, so we use having clause
SELECT ProductName, UnitPrice
	FROM Products
	GROUP BY ProductName, UnitPrice
	HAVING AVG(UnitPrice)>20;

--SELECT Clause
SELECT * FROM Products

SELECT ProductName, UnitPrice
FROM Products

--we can use SELECT for expression evaluation
SELECT 1+1 AS 'Sum'

--combine strings using CONCAT()
SELECT CONCAT(LastName,' ',FirstName) AS FullName
FROM Employees


USE employee_db1
CREATE TABLE EmployeeMaster(
	Id INT IDENTITY PRIMARY KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(25),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT
	);
INSERT INTO EmployeeMaster VALUES
('E0001','Hulk','IT','TVM',4000),
('E0002','Spiderman','IT','TVM',4000),
('E0003','Ironman','QA','KLM',3000),
('E0004','Superman','QA','KLM',3000),
('E0005','Batman','HR','TVM',5000),
('E0006','Raju','HR','KTM',5000),
('E0007','Radha','HR','KTM',5000);

SELECT * FROM EmployeeMaster
--GROUPING SETS Example
SELECT EmployeeCode, EmployeeName, DepartmentCode, LocationCode, SUM(Salary) TotalCost
FROM EmployeeMaster
GROUP BY 
	GROUPING SETS
	(
		(EmployeeCode, EmployeeName, DepartmentCode, LocationCode),
		(DepartmentCode),
		--NULL	NULL	HR	NULL	15000
		--NULL	NULL	IT	NULL	8000
		--NULL	NULL	QA	NULL	6000
		(LocationCode),
		()
	)
--EmployeeCode	EmployeeName	DepartmentCode	LocationCode	TotalCost
--E0003			Ironman			QA				KLM				3000
--E0004			Superman		QA				KLM				3000
--NULL			NULL			NULL			KLM				6000
--E0006			Raju			HR				KTM				5000
--E0007			Radha			HR				KTM				5000
--NULL			NULL			NULL			KTM				10000
--E0001			Hulk			IT				TVM				4000
--E0002			Spiderman		IT				TVM				4000
--E0005			Batman			HR				TVM				5000
--NULL			NULL			NULL			TVM				13000
--NULL			NULL			NULL			NULL			29000
--NULL			NULL			HR				NULL			15000
--NULL			NULL			IT				NULL			8000
--NULL			NULL			QA				NULL			6000


--comparison operator
SELECT * FROM EmployeeMaster WHERE Salary = 3000
SELECT * FROM EmployeeMaster WHERE Salary <> 3000
SELECT * FROM EmployeeMaster WHERE Salary != 3000
SELECT * FROM EmployeeMaster WHERE Salary < 3000
SELECT * FROM EmployeeMaster WHERE Salary <= 3000
SELECT * FROM EmployeeMaster WHERE Salary > 3000
SELECT * FROM EmployeeMaster WHERE Salary >= 3000
SELECT * FROM EmployeeMaster WHERE Salary !> 3000
SELECT * FROM EmployeeMaster WHERE Salary !< 3000

--IN,NOT OPERATORS
SELECT * FROM EmployeeMaster WHERE Salary IN(3000,5000)
SELECT * FROM EmployeeMaster WHERE EmployeeName IN('Raju','Radha')
SELECT * FROM EmployeeMaster WHERE EmployeeName NOT IN('Raju','Radha')

--BETWEEN, NULL, NOT OPERATORS
SELECT * FROM EmployeeMaster WHERE Salary BETWEEN 3000 AND 5000
SELECT * FROM EmployeeMaster WHERE Salary IS NOT NULL
SELECT * FROM EmployeeMaster WHERE Salary IS NULL

--LIKE OPERATORS
--% to match any string of any length
--[] to match on  any character in the [] brackets (eg :[abc] match on a,b, or c)
--[^] used to match on any characters not in the [^] brackets(eg:[^abc] match on charcter not a, b, c)
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Superman'
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Sup%'
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE '%man'
SELECT * FROM EmployeeMaster WHERE EmployeeName NOT LIKE '%man'
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE '%ra%'
--WILDCARD SEARCHES
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Su[pj]erman%'
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'ra[nj]u%'
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'ra[^nj]u%'
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'ra[^nj]%'
SELECT * FROM EmployeeMaster WHERE EmployeeName NOT LIKE 'ra%'

--EXISTS OPERATOR
SELECT * FROM EmployeeMaster WHERE EXISTS
(SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Superman')

USE employee_db1
CREATE TABLE EmployeeMaster2(
	Id INT IDENTITY PRIMARY KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(25),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT
	);
INSERT INTO EmployeeMaster2 VALUES
('E0001','Arun','IT','TVM',5000),
('E0002','Varun','IT','TVM',4000),
('E0003','Kiran','QA','KLM',3050),
('E0004','Superman','QA','KLM',3000),
('E0005','Midhun','HR','TVM',1000),
('E0006','Singh','HR','KTM',6000),
('E0007','Jyothi','HR','KTM',4000);

SELECT * FROM EmployeeMaster2

--UNION OPERATOR
SELECT * FROM EmployeeMaster
UNION
SELECT * FROM EmployeeMaster2
--excluding duplicates we have 13 rows

SELECT * FROM EmployeeMaster
UNION ALL
SELECT * FROM EmployeeMaster2
--including duplicates using UNION ALL we have 14 rows

--UNION using multiple expressions
SELECT EmployeeName,Salary FROM EmployeeMaster
	WHERE Salary>3000
	UNION 
	SELECT EmployeeName,Salary FROM EmployeeMaster2
--While using UNION, we need to specify the same column list for both expressions

--INTERSECT Operator
SELECT * FROM EmployeeMaster
INTERSECT
SELECT * FROM EmployeeMaster2

--INTERSECT using multiple expressions
SELECT EmployeeName,Salary FROM EmployeeMaster
	WHERE Salary>2000
	INTERSECT 
	SELECT EmployeeName,Salary FROM EmployeeMaster2


	SELECT * FROM EmployeeMaster
