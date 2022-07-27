USE emplyoee_db1;
 
 --create a new table employee
 CREATE TABLE employee(
	id INT IDENTITY PRIMARY KEY,
	name VARCHAR(50),
	age SMALLINT,
	location VARCHAR(50)
	);

--To alter an existing table
ALTER TABLE employee
	ADD DOB DATE;

--To descibe the details of the table
EXEC sp_help employee;


--Insert 3 rows into the table
--id value is excluding becz it has constraint IDENTITY which means auto incrementing
-- also specifying column names specifically is also optional
--date format is default like 'yyyy-mm-dd'
INSERT INTO employee
VALUES('Tom',2,'USA', '2019-10-20'),
('Jerry',1,'USA', '2019-03-20'),
('Mickey',3,'USA', '2018-10-22');

--to fetch the data from the table
SELECT * FROM employee

--to update rows of data
UPDATE employee
SET name = 'Donald'
WHERE name = 'Tom';

SELECT * FROM employee

--Delete a record from the table
DELETE FROM employee
WHERE name = 'Donald'

SELECT * FROM employee

--delete a table
DROP TABLE employee


 --create a new table employee
 CREATE TABLE employee(
	id INT IDENTITY PRIMARY KEY,
	name VARCHAR(50),
	age SMALLINT,
	location VARCHAR(50)
	);

--To alter an existing table
ALTER TABLE employee
	ADD DOB DATE;

INSERT INTO employee
VALUES('Tom',2,'USA', '2019-10-20'),
('Jerry',1,'USA', '2019-03-20'),
('Mickey',3,'USA', '2018-10-22');

--UI automatically generated script
--Right click on table, 'script table as'
USE [emplyoee_db1]
GO

INSERT INTO [dbo].[employee]
           ([name]
           ,[age]
           ,[location]
           ,[DOB])
     VALUES
           ('Goofy'
           ,5
           ,'Paris'
           ,'2018-10-19')
GO
--GO is a block delimiter