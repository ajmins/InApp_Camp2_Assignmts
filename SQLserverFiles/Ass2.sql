--AJMI N S

--Question 1) The company has a lot of departments (Accounts, sales, Marketing...).
--Employees of the company belong to one of these departments.
--Every employee will have a manager.
--The following details of the employees also need to be stored (EmployeeID, FirstName, LastName,
--UserID, department, salary, JoiningDate, Designation, Commission).

--Select the databse
USE employee_db1

--Create a table Department
CREATE TABLE Department(
	DeptNo SMALLINT IDENTITY PRIMARY KEY,
	DeptName VARCHAR(20) UNIQUE,
	FloorNo TINYINT,
	LocationName VARCHAR(20)
);
--The two tables are related by the primary key (deptno in Department table) and 
--foreign key (deptno in the Employee table)

--Create a table Employee_det
CREATE TABLE Employee_det (
	Empno INT IDENTITY PRIMARY KEY,
	ManagerID INT,
	FstName VARCHAR(20) NOT NULL,
	LstName VARCHAR(20),
	UserID VARCHAR(20),
	DeptNo SMALLINT FOREIGN KEY REFERENCES Department(DeptNo),
	Salary DECIMAL( 18,2),
	Commission INT,
	JoiningDate DATE,
	Designation VARCHAR(25)
);

--Modify the Employee table structure to add the HRA component width 5 and 2 decimal places.
--Add PF of width 5 and 2 decimal places to the Employee table
ALTER TABLE Employee_det
	ADD HRA DECIMAL(5,2), PF DECIMAL(5,2);

-- add a constraint to the field that the value of the PF
--should not be greater than 5000.
ALTER TABLE Employee_det
	ADD CONSTRAINT chk_pf CHECK(PF<5000);

ALTER TABLE Employee_det
	DROP CONSTRAINT FK__Employee___DeptN__18EBB532;

ALTER TABLE Employee_det
ADD CONSTRAINT fkcst
    FOREIGN KEY (DeptNo)
    REFERENCES Department(DeptNo)
    ON DELETE CASCADE;

--Viewing tables	
SELECT * FROM Department;
SELECT * FROM Employee_det;


--INSERT VALUES into tables
INSERT INTO Department(DeptName, FloorNo ,LocationName) VALUES
('QA', 2, 'A'),
('HR', 3, 'B'),
('IT', 1, 'C'),
('LS', 3, 'D');

INSERT INTO Employee_det VALUES
(110,'Amreet', 'Prasad', 'ap12', 1, 5000, 1, '1995-10-01', 'TE', 100, 600),
(111,'Avant', 'Krishna', 'ak10', 3, 3000, 1, '2000-05-01', 'ASE', 150, 100),
(112,'Jay', 'Surya', 'js11', 4, 4000, 3, '2002-10-01', 'UXE', 110, 200),
(113,'Meera', 'Jasmine', 'mj05', 3, 7000, 4, '2005-05-13', 'SE', 111, 500);

--HRA and PF component has to be added to the salary of all the employees
UPDATE Employee_det
SET Salary = Salary + HRA + PF; 

--Retrieve the details of all employees sorted in the alphabetical order of their name
SELECT * FROM Employee_det
ORDER BY FstName,LstName;

-- Display the details of the employee in the descending order of the income
SELECT * FROM Employee_det
ORDER BY Salary DESC;

--Display the details of all employees whose name starts with ‘A’ has ‘e’ in it and ends with ‘t’.
SELECT * FROM Employee_det
WHERE FstName LIKE 'a%[e]%t'

--Display the details of all employees who joined after ’01-Jan-98’ and whose salary is higher than 25000
SELECT * FROM Employee_det
WHERE JoiningDate > '1998-01-01' AND Salary > 25000


--Question 2 customers place orders for items.
--The order is placed in a particular date. A single order can have multiple items. In the order the item name and the quantity ordered will be mentioned.

--Create a table Customer_tb
CREATE TABLE Customer_tb(
	CustNo SMALLINT PRIMARY KEY,
	CustName VARCHAR(20),
	CustAddress VARCHAR(40)
);
--Create a table Order_tb
CREATE TABLE Order_tb(
	OrdNo SMALLINT PRIMARY KEY,
	CustNo SMALLINT FOREIGN KEY REFERENCES Customer_tb(CustNo),
	OrderDate DATE
);
--Create a table OrderItem_tb
CREATE TABLE OrderItem_tb(
	ItemID SMALLINT PRIMARY KEY,
	OrdNo SMALLINT FOREIGN KEY REFERENCES Order_tb(OrdNo),
	ItemName VARCHAR(20),
	Quantity SMALLINT
);










