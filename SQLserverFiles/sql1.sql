--AJMI N S
--QUESTION 1

--EmployeeDetails Table
--+--------+----------+--------+------------+
-- | emp_id | emp_name | pay | dept_name |
-- +--------+----------+--------+-----------+
-- | 001 | Dilip | 3000 | IT |
-- | 002 | Fahad | 4000 | Sales |
-- | 003 | Lal | 6000 | Marketing |
-- | 004 | Nivin | 2000 | IT |
-- | 005 | Vijay | 9000 | Sales |
-- | 006 | Anu | 5000 | HR |
-- | 007 | Nimisha | 5000 | Sales |
-- | 008 | Praveena | 8000 | Marketing |
-- +--------+----------+--------+-----------+

--Normalize
-----------
--The table into its 3rd Normal form. Create necessary sub-tables

USE employee_db1

--Create a table Department
CREATE TABLE DeptDetails(
	DeptNo SMALLINT PRIMARY KEY,
	DeptName VARCHAR(25)
);

--Create a table EmployeeDetails
CREATE TABLE EmployeeDetails(
	emp_id SMALLINT PRIMARY KEY,
	emp_name VARCHAR(20),
	pay INT,
	DeptNo SMALLINT FOREIGN KEY REFERENCES DeptDetails(DeptNo),
);

--Insert values into tables
INSERT INTO DeptDetails VALUES
(1, 'IT'), (2, 'Sales'), (3, 'Marketing'), (4, 'HR');

INSERT INTO EmployeeDetails VALUES
(001, 'Dilip', 3000, 1),
(002, 'Fahad', 4000, 2),
(003, 'Lal', 6000, 3),
(004, 'Nivin', 2000, 1),
(005, 'Vijay', 9000, 2),
(006, 'Anu', 5000, 4),
(007, 'Nimisha', 5000, 2),
(008, 'Praveena', 8000, 3);

--view values
SELECT * FROM DeptDetails;
SELECT * FROM EmployeeDetails;
---------------------------------------------------------------------
--QUERIES--
----------------------------------------------------------------------

--1) The total number of employees.
SELECT COUNT(emp_id) AS 'Total Number'
	FROM EmployeeDetails;
		--8

--2) Total amount required to pay all employees.
SELECT SUM(pay) AS 'Total amount'
	FROM EmployeeDetails;
		--42000

--3) Average, minimum and maximum pay in the organization.
SELECT AVG(pay) AS 'Average amount', MIN(pay) AS 'Minimum Amount', MAX(pay) AS 'Maximum Amount'
	FROM EmployeeDetails;
			--Average amount	Minimum Amount	Maximum Amount
			--5250				2000			9000

--4) Each Department wise total pay
SELECT EmployeeDetails.DeptNo, DeptName , SUM(pay) AS 'AmountByDept' 
	FROM EmployeeDetails
	 JOIN DeptDetails ON EmployeeDetails.DeptNo = DeptDetails.DeptNo
	GROUP BY EmployeeDetails.DeptNo, DeptName;
				--DeptNo	DeptName	AmountByDept
				--1	IT	5000
				--2	Sales	18000
				--3	Marketing	14000
				--4	HR	5000

--5) Average, minimum and maximum pay department-wise.
SELECT EmployeeDetails.DeptNo, DeptName , AVG(pay) AS 'Average amount', MIN(pay) AS 'Minimum Amount', MAX(pay) AS 'Maximum Amount' 
	FROM EmployeeDetails
	 JOIN DeptDetails ON EmployeeDetails.DeptNo = DeptDetails.DeptNo
	GROUP BY EmployeeDetails.DeptNo, DeptName;
					--DeptNo	DeptName	Average amount	Minimum Amount	Maximum Amount
					--1	IT	2500	2000	3000
					--2	Sales	6000	4000	9000
					--3	Marketing	7000	6000	8000
					--4	HR	5000	5000	5000


--6) Employee details who earns the maximum pay.
SELECT *
	FROM EmployeeDetails
	WHERE pay = (SELECT MAX(pay) 
					FROM EmployeeDetails)
			--emp_id	emp_name	pay	DeptNo
			--5			Vijay		9000	2





--7) Employee details who is having a maximum pay in the department.
---------------------
SELECT *
FROM EmployeeDetails
WHERE pay IN
    (SELECT MAX(pay)
     FROM EmployeeDetails
     WHERE DeptNo IN
         (SELECT d.DeptNo
          FROM DeptDetails d
				GROUP BY DeptNo	));
------------------------------

--9) Employee who has more pay than the average pay of his department.

------------------------------------------------

---------------------------------------


--10)Unique departments in the company
SELECT DISTINCT DeptName FROM EmployeeDetails 
	 JOIN DeptDetails ON EmployeeDetails.DeptNo = DeptDetails.DeptNo
				-- DeptName
				--HR
				--IT
				--Marketing
				--Sales

--11)Employees In increasing order of pay
SELECT emp_name, pay
	FROM EmployeeDetails
	ORDER BY pay;
			--emp_name	pay
			--Nivin	2000
			--Dilip	3000
			--Fahad	4000
			--Anu	5000
			--Nimisha	5000
			--Lal	6000
			--Praveena	8000
			--Vijay	9000


--12)Department In increasing order of pay
SELECT DeptName, pay FROM EmployeeDetails 
	 JOIN DeptDetails ON EmployeeDetails.DeptNo = DeptDetails.DeptNo
	 ORDER BY pay DESC;
				--DeptName	pay
				--Sales	9000
				--Marketing	8000
				--Marketing	6000
				--HR	5000
				--Sales	5000
				--Sales	4000
				--IT	3000
				--IT	2000

--DEPTWISE SUM
SELECT EmployeeDetails.DeptNo, DeptName , SUM(pay) AS 'AmountByDept' 
	FROM EmployeeDetails
	JOIN DeptDetails ON EmployeeDetails.DeptNo = DeptDetails.DeptNo
	GROUP BY EmployeeDetails.DeptNo, DeptName 
	ORDER BY (SUM(PAY)) DESC;
	
				--DeptNo	DeptName	AmountByDept
				--2	Sales	18000
				--3	Marketing	14000
				--4	HR	5000
				--1	IT	5000