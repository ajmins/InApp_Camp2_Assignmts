--11th July 2022
--SQL STRING FUNCTIONS

--American Standard Code for Information Interchange(ASCII)
SELECT ASCII('A') AS 'ASCII Value'
		--ASCII Value
		--65

--Position of first occurance
SELECT CHARINDEX('World','Hello World') AS 'Position' 
		--Position
		--7
SELECT CHARINDEX('Wold','Hello World') AS 'Position' 
		--Position
		--0

--Join two strings
SELECT CONCAT('Hello', ' World') AS 'Combined word' 
		--Combined word
		--Hello World

-- Using SOUNDEX to check how the two strings sound similar
SELECT SOUNDEX ('Smith'), SOUNDEX ('Smythe');
		--S530	S530
SELECT SOUNDEX ('Test'), SOUNDEX ('Testing');
		--T230	T235
SELECT SOUNDEX ('Tom'), SOUNDEX ('Toum');
		--T500	T500

--The DIFFERENCE function compares the difference of the SOUNDEX pattern results. 
SELECT DIFFERENCE ('Test', 'Testing');
		--3
		--the strings differ in 3 letters
SELECT DIFFERENCE ('Tom', 'Toum');
		--4
SELECT DIFFERENCE ('Goat', 'Primose');
		--0

--0 indicates weak or no similarity between the SOUNDEX values. 
--4 indicates strong similarity or identically SOUNDEX values.


SELECT LEFT('Hello World',5), RIGHT('Hello World',5);
		--Hello	World
		--specific number of characters from the left side or right side is displayed
SELECT LEFT('Hello World',2), RIGHT('Hello World',4);
		--He	orld

--12th July 2022
--LOWER().UPPER(),LTRIM(),RTRIM(),REPLICATE()

--converting string to lower case and upper case
SELECT LOWER('Hello'), UPPER('Hello');
		--hello	HELLO

--trim unwanted space from left or right or both
SELECT TRIM(' HEllo '); --HEllo
SELECT LTRIM('Hello  '); --Hello  
SELECT LTRIM('   Hello  '); --Hello  
SELECT RTRIM('   World'); --   World
SELECT RTRIM('   World   '); --   World

--duplicate a string in specified number of times
SELECT REPLICATE(' Hello' ,3) AS 'Result';
		-- Hello Hello Hello

--SQL Date & Time 
--retuen current time stamp
SELECT CURRENT_TIMESTAMP AS 'Date'; --2022-07-12 09:58:03.143
--return current date time
SELECT GETDATE() AS 'Date'; --2022-07-12 09:58:03.143
--get the UTC date
SELECT GETUTCDATE() AS 'Date'; --2022-07-12 04:28:03.140
--get the precise time (nanosecond)
SELECT SYSDATETIME() AS 'Date'; --2022-07-12 09:58:03.1429823

--DATENAME(), DATEPART()
--EXTRACTING THE PART OF DATE
--to extract the part of date day, month or year
--returns as STRING
SELECT DATENAME(day, '2000/05/13') AS 'Day'; --13
SELECT DATENAME(month, '2000/05/13') AS 'Month'; --May
SELECT DATENAME(year, '1995/01/10') AS 'Year'; --1995


--to extract the part of the date as an INTEGER
SELECT DATEPART(day, '2000/05/13') AS 'Day'; --13
SELECT DATEPART(month, '2000/05/13') AS 'Month'; --5
SELECT DATEPART(year, '1995/01/10') AS 'Year'; --1995

SELECT DAY('2000/05/13') AS 'Day'; --13
SELECT MONTH('2000/05/13') AS 'Day'; --5
SELECT YEAR('2000/05/13') AS 'Day'; --2000

--DATEDIFF
--to extract the difference of days , months or years
SELECT DATEDIFF(DD,'1995/01/10','2000/05/13') AS 'Total Days'; --1950 days
SELECT DATEDIFF(MM,'1995/01/10','2000/05/13') AS 'Total Months'; --64 months
SELECT DATEDIFF(WK,'1995/01/10','2000/05/13') AS 'Total Weeks'; --278 weeks
SELECT DATEDIFF(YY,'1995/01/10','2000/05/13') AS 'Total Years'; --5 years

--MATHEMATICAL FUNCTIONS
--to find the square root
SELECT SQRT(25) AS 'squareRoot'; --5
--to find the Absolute value without sign
SELECT ABS(-20) AS 'absoluteValue'; --20
--to find the next highest value
SELECT CEILING(13.5) AS 'roundhigh'; --14
--to find the next lowets value
SELECT FLOOR(10.5) AS 'roundLow'; --10
--to find the power (exponenetial)
SELECT POWER(3,2) AS 'power'; --9
--to find the natural log
SELECT LOG(25) AS 'naturalLog'; --3.2188758248682
--to find the sign pf the integer
SELECT SIGN(-25) AS 'numberSign'; -- (-1)
SELECT SIGN(25) AS 'numberSign'; -- (1)

--RAND() FUNCTION
--to generate a psuedo random number, becaue system uses some calculation (not a pure random)
SELECT RAND() AS 'randomNumber'; --0.148246766383427
SELECT RAND() AS 'randomNumber'; --0.748037614759373

--to generate a psuedo random number with a seed
--same random number but do not change always irrespective of the computers
SELECT RAND(10) AS 'randomNumber'; --0.713759689954247
SELECT RAND(10) AS 'randomNumber'; --0.713759689954247
--
SELECT RAND(5) AS 'randomNumber'; --0.713666525097956
SELECT RAND(5) AS 'randomNumber'; --0.713666525097956
--
SELECT RAND(1501) AS 'randomNumber'; --0.741541450100224

--SQL CONVERSION FUNCTIONS
--CONVERT() is MSSQL specific
--syntax: CONVERT(dest_data_type,expression_2_convert, length)
--convert expression to int
SELECT CONVERT(int, 30.55); --30
--convert string expression to datetime
SELECT CONVERT(datetime, '2000-05-13'); --2000-05-13 00:00:00.000
--convert to varchar of length 100
SELECT CONVERT(varchar, '2000-05-13', 101); --2000-05-13

--CAST() is also similar to CONVERT but is ANSI 
--syntax: CAST(expression_2_convert AS dest_data_type)
--convert expression to varchar
SELECT CAST(20.65 AS varchar); --20.65
--converts a value to a datetime datatype
SELECT CAST('2000-05-13' AS datetime); --2000-05-13 00:00:00.000

--SQL JOINS
--INNER JOIN, OUTER JOIN, SELF JOIN, CROSS JOIN
--OUTER JOIN --> LEFT OUTER, RIGHT OUTER AND FULL OUTER

--JOINS
--Creating a new database
CREATE DATABASE training
USE training;

--Creating three tables 
CREATE TABLE trainee (
	id INT PRIMARY KEY IDENTITY,
	admsn_no VARCHAR(45) NOT NULL,
	fstName VARCHAR(45) NOT NULL,
	lstName VARCHAR(45) NOT NULL,
	age INT,
	city VARCHAR(25) NOT NULL
	);
CREATE TABLE fee (
	admsn_no VARCHAR(45) NOT NULL,
	sem_no INT NOT NULL,
	course VARCHAR(45) NOT NULL,
	amount INT
	);

CREATE TABLE semester (
	sem_no INT NOT NULL,
	sem_name VARCHAR(10)
	);

--Insert values
INSERT INTO trainee (admsn_no, fstName, lstName, age, city) VALUES
(3354,'Spider','Man', 13, 'Texas'),
(2135,'James','Bond', 15, 'Alaska'),
(4321,'Jack','Sparrow', 14, 'California'),
(4213,'John','McClane', 17, 'New York'),
(5112,'Optimus','Prime', 16, 'Florida'),
(6113,'Captain','Kirk', 15, 'Arizona'),
(7555,'Harry','Potter', 14, 'New York'),
(8345,'Rose','Dawson', 13, 'California');

SELECT * FROM trainee --8 rows

INSERT INTO semester (sem_no,sem_name) VALUES
(1,'First Sem'),
(2,'Second Sem'),
(3,'Third Sem'),
(4,'Fourth Sem');

SELECT * FROM semester --4 rows

INSERT INTO fee (admsn_no, sem_no, course, amount) VALUES
(3354, 1, 'Java', 20000),
(7555, 1, 'Android', 22000),
(4321, 2, 'Python', 18000),
(8345, 2, 'SQL', 15000),
(9345, 2, 'Blockchain', 16000),
(9321, 3, 'Ethical Hacking', 17000),
(5112, 1, 'Machine Learning', 30000);

SELECT * FROM fee --7 rows

--INNER JOIN
--default join returns records matching with both values
SELECT * FROM trainee
	INNER JOIN fee ON trainee.admsn_no = fee.admsn_no;

SELECT trainee.admsn_no, trainee.fstName, trainee.lstName, fee.course,fee.amount 
	FROM trainee
	INNER JOIN fee ON trainee.admsn_no = fee.admsn_no;

--inner join with 3 tables
SELECT trainee.admsn_no, trainee.fstName, trainee.lstName, fee.course,fee.amount, semester.sem_name 
	FROM trainee
	INNER JOIN fee ON trainee.admsn_no = fee.admsn_no
	INNER JOIN semester ON semester.sem_no = fee.sem_no;

--Outer Join
--Left Outer Join or Left Join
--Left Join: returns all the values from the left table(trainee), even if there is no matching values with right table(fee)
--Return NULL for records that do not match
SELECT * FROM trainee
	LEFT JOIN fee ON trainee.admsn_no = fee.admsn_no;

SELECT trainee.admsn_no,trainee.fstName,trainee.lstName,fee.course, fee.amount 
	FROM trainee
	LEFT JOIN fee ON trainee.admsn_no = fee.admsn_no;

--Right Outer Join or Right Join
--Right Join: returns all the values from the right table(fee), even if there is no matching values with left table(trainee)
--Return NULL for records that do not match
SELECT * FROM trainee
	RIGHT JOIN fee ON trainee.admsn_no = fee.admsn_no;

SELECT trainee.admsn_no,trainee.fstName,trainee.lstName,fee.course, fee.amount 
	FROM trainee
	RIGHT JOIN fee ON trainee.admsn_no = fee.admsn_no;

--Full Outer Join or Full Join
--Full Join returns all the rows from both tables
--Return NULL for record that do not match
SELECT * FROM trainee
	FULL JOIN fee ON trainee.admsn_no = fee.admsn_no;

SELECT trainee.admsn_no,trainee.fstName,trainee.lstName,fee.course, fee.amount  
	FROM trainee
	FULL JOIN fee ON trainee.admsn_no = fee.admsn_no;

--SELF JOIN: a table is joined to itself
--we are giving aliasing names t1 and t2 for the same table itself
--Used to extract the hierachical data and comparing rows inside a single table since it is a combination of 2 copies of the same table
--To list people in order of city, based on admsn no and city
SELECT t1.fstName, t1.lstName, t2.city
	FROM trainee t1, trainee t2
	WHERE t1.admsn_no = t2.admsn_no
	AND t1.city = t2.city
	ORDER BY t2.city;

SELECT t1.admsn_no, t1.fstName, t1.lstName, t2.city, t2.admsn_no 
	FROM trainee t1, trainee t2
	WHERE t1.admsn_no = t2.admsn_no
	AND t1.city = t2.city
	ORDER BY t2.city;

--same city but different admsn number
--repeating list of cities
SELECT t1.fstName, t1.lstName, t2.city 
	FROM trainee t1, trainee t2
	WHERE t1.admsn_no <> t2.admsn_no
	AND t1.city = t2.city
	ORDER BY t2.city;

SELECT t1.admsn_no, t1.fstName, t1.lstName, t2.city, t2.admsn_no 
	FROM trainee t1, trainee t2
	WHERE t1.admsn_no <> t2.admsn_no
	AND t1.city = t2.city
	ORDER BY t2.city;

--CROSS JOIN : result is the cartesian product of two tables 
--obtained by multiplying all the number of rows in table 1 to all the rows in table 2
SELECT *
	FROM trainee
	CROSS JOIN fee
	--total 8 x 7 = 56 rows

--if we use WHERE caluse with CROSS JOIN then it behaves like an INNER Join
SELECT trainee.admsn_no, trainee.fstName, trainee.lstName,fee.course, fee.amount
	FROM trainee
	CROSS JOIN fee
	WHERE trainee.admsn_no = fee.admsn_no;

--Stored Procedure 
--A stored procedure is a group of SQL statements compiled into a single execution plan
--It is compiled once and can be used again and again.

--Creating a stored procedure
CREATE PROCEDURE traineeAgeWiseList
AS
BEGIN
	SELECT fstName,age,city
	FROM trainee
	ORDER BY age;
END;

--Executing SP
EXEC traineeAgeWiseList;

--Modifying SP
ALTER PROCEDURE traineeAgeWiseList
AS
BEGIN
	SELECT admsn_no, fstName,lstName,age,city
	FROM trainee
	ORDER BY age;
END;

--Listing all the SP in current db
SELECT * FROM sys.procedures

--Deleting the SP
DROP PROCEDURE traineeAgeWiseList

--Adding parameters in the SP
--@city datatype is the parameter
--no keyword like INPUT
CREATE PROCEDURE getTraineesFromCity(@city VARCHAR(50))
AS
BEGIN
	SET NOCOUNT ON; -- will disable the count of rows affected like "1 row affected", "2 row affected" etc
	SELECT fstName, lstName, age,city
	FROM trainee
	WHERE city = @city;
END;

SELECT city FROM trainee;

--Execute the SP
EXEC getTraineesFromCity 'Alaska'

--Return parameters from SP
--use keyword OUTPUT
CREATE PROCEDURE getTraineeCount (@traineeCount INT OUTPUT)
AS
BEGIN
	SELECT @traineeCount = COUNT(id)
	FROM trainee;
END;

--To run the procedure
--Receiving output from SP
--Run all three steps in a single step
--step1 Declare the variable to hold the output
DECLARE @Trainee_Count INT
--step2 Executing the stored procedure using the keyword OUTPUT
EXEC getTraineeCount @Trainee_Count OUTPUT
--step3 To print the result
PRINT @Trainee_Count --8

--SubQuery
--A subquery is a query that is nested inside a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery.
--embedded within the WHERE clause

SELECT *
FROM trainee
WHERE id IN (SELECT id FROM trainee
				WHERE age>15);

--SubQuery with DELETE 
DELETE
	FROM trainee
	WHERE admsn_no IN (
		SELECT admsn_no
		FROM trainee
		WHERE admsn_no = 3354) ;

SELECT * FROM trainee

--VIEWS IN SQL
--A virtual Table  based on the result-set of an SQL statement

--Creating a view
CREATE VIEW [New York trainees] AS
	SELECT fstName, lstName, city
	FROM trainee
	WHERE city = 'New York' ;

--to query the view
SELECT * FROM [New York trainees];

--SQL Trigger
--SQL trigger is a database object which fires when an event occurs in a database.
--We can execute a SQL query that will do a 'process' when a change occurs on a database table such as insertion, updating, deletion etc
--Two types : DDL Trigger & DML Trigger

--DDL Trigger
--Fired in response to DDL (Data Definition Language) events like Create, Alter and Drop
--Is applied to the whole database
CREATE TRIGGER 	dontPlayWithMyDb
	ON DATABASE
	FOR
	create_table, alter_table, drop_table --these events on the db 
	AS --trigger execution statements
	PRINT 'These operations are not allowed in this database '
	ROLLBACK; --Roll back to previous state

--to check the functionality of this trigger
--create a table
CREATE TABLE testTable (
	id INT
	);
--The transaction ended in the trigger. The batch has been aborted.

--delete the trigger
DROP TRIGGER dontPlayWithMyDb 
	ON DATABASE;

DROP TABLE testTable;
--These operations are not allowed in this database 
--Msg 3609, Level 16, State 2, Line 427
--The transaction ended in the trigger. The batch has been aborted.

--DML Trigger: Fired in response to DML (Data Manipulation Language) events like Insert, Update, and Delete.
--Affecting the Table
--DML -> AFTER Trigger
--AFTER triggers are executed after the action of an INSERT, UPDATE, or DELETE statement.
--After the AFTER triggers are executed after the action of INSERT, we are trying to automatically save a copy of values to the backup table.
CREATE TRIGGER msgAfterInsert
ON trainee
AFTER INSERT AS
BEGIN
	PRINT 'Inserted fine' 
END;

--To test the trigger insert some values into table trainee
INSERT INTO trainee VALUES
(3854,'Super','Man', 10, 'Texas')
		--Inserted fine
		--HERE event is happened then only trigger function

--Drop trigger
DROP TRIGGER msgAfterInsert

--DML : AFTER Trigger : Automatic value insertion
--: After the AFTER triggers are executed after the action of INSERT, we are trying to automatically save a copy of values to the backup table.

--create a new table to save the backup as backup table
CREATE TABLE traineeBackup (
	id INT PRIMARY KEY IDENTITY,
	admsn_no VARCHAR(45) NOT NULL,
	fstName VARCHAR(45) NOT NULL,
	lstName VARCHAR(45) NOT NULL,
	age INT,
	city VARCHAR(25) NOT NULL
	);

--AFTER Trigger : Automatic value insertion
CREATE TRIGGER backupTrainees
ON trainee
AFTER INSERT
AS
BEGIN
	SET NOCOUNT ON; --do no show the number of affected rows
	--declare the variables to hold the trainee table values
	DECLARE @id INT
	DECLARE @admsn_no INT
	DECLARE @fstName VARCHAR(45)
	DECLARE @lstName VARCHAR(45)
	DECLARE @age INT
	DECLARE @city VARCHAR(25)

	SELECT @id = I.id,
	@admsn_no = I.admsn_no,
	@fstName = I.fstName,
	@lstName = I.lstName,
	@age = I.age,
	@city = I.city
	FROM INSERTED I 
	--INSERTED property gives the inserted values
	--I is the handle used
	--here @id is not needed because it's declared as a IDENITITY
	INSERT INTO traineeBackup VALUES
	(@admsn_no, @fstName, @lstName, @age, @city)

	PRINT 'Values inserted in trainee and backup tables'
END;
--Insert values
INSERT INTO trainee (admsn_no, fstName, lstName, age, city) VALUES
(2354,'Bat','Man', 12, 'Texas');

SELECT * FROM trainee
SELECT * FROM traineeBackup

--drop 
DROP TRIGGER backupTrainees

--DML : INSTEAD OF Trigger
--The database engine will execute only the trigger instead of executing the statement.
CREATE TRIGGER doInsteadOfInsert
ON trainee
INSTEAD OF INSERT
AS
BEGIN
	PRINT 'Values Not Inserted because of a trigger!!!'
END

INSERT INTO trainee (admsn_no, fstName, lstName, age, city) VALUES
(2374,'Hit','Man', 12, 'Texas');
--Values Not Inserted

--difference between AFTER and INSTEAD OF is that in AFTER, the trigger is executed after the insertion has been done but 
-- in the case of INSTEAD OF will not insert the values rather the trigger is executed

--13th July 2022
--SQL SERVER TRANSACTIONS
--Transaction in SQL is a sequential DML stmts to  perform single or multiple tasks
--COMMITTED: all modifications were susscessful
--ROLLBACK: all modification are undone

--COMMIT of Transaction
--To strat a new transaction
BEGIN TRANSACTION
	--SQL statements
	INSERT INTO semester VALUES (5,'sem 5') --query 1
	UPDATE semester SET sem_name = 's5' 
	WHERE sem_no = 5; --query2
--Commit changes and transactions
COMMIT TRANSACTION

--ROLLBACK of Transaction
--To strat a new transaction
BEGIN TRANSACTION
	--SQL statements
	INSERT INTO semester VALUES (6,'sem 6') --query 1
	UPDATE semester SET sem_name = 's6' 
	WHERE sem_no = 6; --query2
--Rollback changes and transactions
ROLLBACK TRANSACTION

SELECT * FROM semester;

--ROLLBACK on transaction error with more control
BEGIN TRANSACTION
	INSERT INTO semester VALUES (6, 'Sem 6') --query1
	UPDATE semester SET sem_no = 'six' WHERE sem_no = 6; --query 2 with error
--Check for an eroror using system variable @@ERROR
--@@ERROR = 0 then no error; else if any non zero value the error
IF(@@ERROR > 0)
	BEGIN
		ROLLBACK TRANSACTION
	END
ELSE
	BEGIN
		--print @@error
		COMMIT TRANSACTION
	END
	--Conversion failed when converting the varchar value 'six' to data type int.

--ROLLBACK on transaction error automatically
BEGIN TRANSACTION
	INSERT INTO semester VALUES (6, 'Sem 6') --query 1
	UPDATE semester SET sem_no = 'six' WHERE sem_no = 6; --query 2 with error
--will try to commit transaction, if fails, wil automatically rollback
COMMIT TRANSACTION

--------------ended--------------------










