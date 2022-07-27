--SQL ASSIGNMENT 1
--1. Create a 'sales' Table
--2. OrderID is the PRIMARY KEY
--3. DEFAULT ordQty is 1 and DEFAULT date is today's date
--4. Check custName for NOT NULL
--TABLE
--+---------+------------+------------+---------------+--------------+
--| orderID | ordDate | ordPrice | ordQty | custName |
--+---------+------------+------------+---------------+--------------+
--| 1 | 2020/11/22 | 150 | 2 | John |
--| 2 | 2020/07/10 | 180 | 2 | Tom |
--| 3 | 2020/06/13 | 400 | 5 | Jerry |
--| 4 | 2020/06/15 | 320 | 2 | John |
--| 5 | 2020/11/22 | 800 | 4 | Bond |
--| 6 | 2020/09/02 | 730 | 4 | Chaplin |
--| 7 | 2020/10/03 | 1000 | 2 | Mickey |
--+---------+------------+------------+---------------+----------+

--Select the databse
USE employee_db1

-- Create a new table
CREATE TABLE sales(
	OrderID INT IDENTITY PRIMARY KEY,
	ordDate DATE DEFAULT GETDATE(),
	ordPrice INT,
	ordQty SMALLINT DEFAULT 1,
	custName VARCHAR(50) NOT NULL
);

--Insert values into the table
INSERT INTO sales VALUES
('2020/11/22', 150, 2, 'John'),
('2020/07/10', 180, 2, 'Tom'),
('2020/06/13', 400, 5, 'Jerry'),
('2020/06/15', 320, 2, 'John'),
('2020/11/22', 800, 4, 'Bond'),
('2020/09/02', 730, 4, 'Chaplin'),
('2020/10/03', 1000, 2, 'Mickey');

--To fetch the data from the table
SELECT * FROM sales

--Write the following queries for sales table:

--1. Count orders made by John.
SELECT COUNT(OrderID) AS 'Order by John'
	FROM sales
	WHERE custName LIKE 'John';
			--Order by John
			--2

--2. Number of unique customers.
SELECT COUNT(DISTINCT custName) AS 'Unique customer count'
	FROM sales
			--Unique customer count
			--6

--3. Total no. of items ordered by all.
SELECT SUM(ordQty) AS 'Total no of items'
	FROM sales
			--Total no of items
			--21

--4. Avg number of items per order.
SELECT AVG(ordQty) AS 'Average Number of items per Order' 
	FROM sales
			--Average Number of items per Order
			--3

--5. Avg Order Quantity with Order Price > 300
SELECT AVG(ordQty) AS 'Average OrderQuantity' 
	FROM sales
	WHERE ordPrice >300;
			--Average OrderQuantity
			--3

--6. Minimum price paid for any of the orders.
SELECT MIN(ordPrice) AS 'Minimum Price'
	FROM sales
			--Minimum Price
			--150

--7. All customers whose name ends with 'n'
SELECT custName
	FROM sales 
	WHERE custName LIKE '%n'
			--custName
			--John
			--John
			--Chaplin

--8. All unique customer's name from the table.
SELECT DISTINCT custName 
	FROM sales
			--custName
			--Bond
			--Chaplin
			--Jerry
			--John
			--Mickey
			--Tom

--9. Total amount spent by each customers.
SELECT SUM(ordPrice) AS 'Total Amount'
	FROM sales
			--Total Amount
			--3580
--OR
SELECT custName, SUM(ordPrice) AS 'Total Amount'
	FROM sales
	GROUP BY custName
			--custName	Total Amount
			--Bond		800
			--Chaplin	730
			--Jerry		400
			--John		470
			--Mickey	1000
			--Tom		180

--10. Unique customers, who have spent more than 700
SELECT DISTINCT custName 
	FROM sales
	WHERE ordPrice > 700
			--custName
			--Bond
			--Chaplin
			--Mickey

--11. Customers that have ordered more than 3 items
SELECT custName 
	FROM sales
	WHERE ordQty > 3
			--custName
			--Jerry
			--Bond
			--Chaplin

--12. All who spent more than 600
SELECT custName 
	FROM sales
	WHERE ordPrice > 600
		--	custName
		--Bond
		--Chaplin
		--Mickey

--13. List orders in ascending order of price.
SELECT OrderID,ordPrice,custName 
	FROM sales
	ORDER BY ordPrice;
		--OrderID	ordPrice	custName
		--1			150			John
		--2			180			Tom
		--4			320			John
		--3			400			Jerry
		--6			730			Chaplin
		--5			800			Bond
		--7			1000		Mickey

--14. List orders in descending order of price.
SELECT OrderID,ordPrice,custName 
	FROM sales
	ORDER BY ordPrice DESC;
		--OrderID	ordPrice	custName
		--7			1000		Mickey
		--5			800			Bond
		--6			730			Chaplin
		--3			400			Jerry
		--4			320			John
		--2			180			Tom
		--1			150			John