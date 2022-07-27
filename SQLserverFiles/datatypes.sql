--DATATYPES
USE employee_db1
CREATE TABLE data_types_eg(
	bit_col BIT,
	char_col CHAR(3),
	date_col DATE,
	date_time_col DATETIME2(3),
	date_time_offset_col DATETIMEOFFSET(2),
	dec_col DECIMAL(4,2),
	num_col NUMERIC(4,2),
	bigint_col BIGINT,
	int_col INT,
	smallint_col SMALLINT,
	tinyint_col TINYINT,
	nchar_col NCHAR(10),
	time_col TIME(0),
	varchar_col VARCHAR(10)
	);
INSERT INTO data_types_eg VALUES(
	1, 
	'ABC', 
	'2022-07-08', 
	'2022-07-08 12:47:50', 
	'2022-07-08 12:47:50 +05:30',
	10.23, 
	15.36, 
	69823548254782989, 
	676874619, 
	28755, 
	250, 
	N'你好', 
	'12:47:50', 
	'hELLO'
	);

SELECT * FROM data_types_eg

USE employee_db1
--Primar Key constraint
--setting primary key for a single column
CREATE TABLE usage_logs(
	logid INT NOT NULL IDENTITY PRIMARY KEY,
	message char(255) NOT NULL
	);

--setup primary key for multiple columns
CREATE TABLE customer_orderdetails(
	OrderID INT NOT NULL,
	ProductID INT NOT NULL,
	UnitPrice decimal(19,4) NOT NULL,
	Quantity smallint NOT NULL,
	PRIMARY KEY(OrderID, ProductID),
	);

--setup primary key using ALTER TABLE
--we need to specify the key name with some contraint name(here crick_id_pk)
CREATE TABLE cricketers(
	crick_id INT NOT NULL,
	lastName VARCHAR(50) NOT NULL,
	firstName VARCHAR(50) NOT NULL,
	salary MONEY
	);
ALTER TABLE cricketers ADD CONSTRAINT
crick_id_pk PRIMARY KEY(crick_id)

--To view Primary key ID
EXEC sp_help cricketers

--NOT deleting or creating pk but just enable or disable pk
--DISABLE PRIMARY KEY
ALTER INDEX crick_id_pk ON cricketers DISABLE;
--ENABLE PRIMARY KEY
ALTER INDEX crick_id_pk ON cricketers REBUILD;

--To remove/delete PK
ALTER TABLE cricketers
	DROP CONSTRAINT crick_id_pk

--Foreign Key
--creating a table with primary key
CREATE TABLE myproducts(
	product_id INT NOT NULL IDENTITY,
	product_name VARCHAR(50) NOT NULL,
	category VARCHAR(25)
	CONSTRAINT myproducts_pk PRIMARY KEY(product_id, product_name)
);

--creating a table with two foreign keys which refer the two primary keys
CREATE TABLE myinventory(
	inventory_id INT PRIMARY KEY,
	product_id INT NOT NULL,
	product_name VARCHAR(50) NOT NULL,
	quantity INT,
	min_level INT,
	max_level INT,
	CONSTRAINT myinventory_fk
		FOREIGN KEY(product_id, product_name)
		REFERENCES myproducts(product_id, product_name)
);
--Disable/Enable Foreign Keys
--Enable Foreign Keys
ALTER TABLE myinventory
	CHECK CONSTRAINT myinventory_fk;
--Disable Foreign Keys
ALTER TABLE myinventory
	NOCHECK CONSTRAINT myinventory_fk;

--Drop/delete FK
ALTER TABLE myinventory
	DROP CONSTRAINT myinventory_fk;

INSERT INTO usage_logs Values
('test');
SELECT * FROM usage_logs
INSERT INTO usage_logs Values
(' ');
INSERT INTO usage_logs Values
(NULL);
--Cannot insert the value NULL into column 'message', table 'employee_db1.dbo.usage_logs'; column does not allow nulls. INSERT fails.
--The statement has been terminated.

--TO CHNAGE A COLUMN TO NOT NULL OR REMOVE THE NOT NULL CONSTRAINT USING ALTER COMMAND
ALTER TABLE usage_logs
ALTER COLUMN message
CHAR(200) NULL;

INSERT INTO usage_logs Values
(NULL);
--Remove/Drop Null
ALTER TABLE usage_logs
ALTER COLUMN message
CHAR(200) NOT NULL;
--Cannot insert the value NULL into column 'message', table 'employee_db1.dbo.usage_logs'; column does not allow nulls. UPDATE fails.
--The statement has been terminated.
--so remove all values including that null vales by truncating the table
TRUNCATE TABLE usage_logs
ALTER TABLE usage_logs
ALTER COLUMN message
CHAR(200) NOT NULL;

--UNIQUE CONSTRAINT
--Set UNIQUE CONSTRAINT during table creation
CREATE TABLE usage_logs(
	logid INT UNIQUE,
	message char(250)
	);
INSERT INTO usage_logs VALUES
(NULL,'test')
SELECT * FROM usage_logs

--remove unique constraint
ALTER TABLE usage_logs
	DROP CONSTRAINT UQ__usage_lo__7838F264576C9B48
INSERT INTO usage_logs VALUES
(NULL,'test')
SELECT * FROM usage_logs
TRUNCATE TABLE usage_logs

--ADD UNIQUE CONSTRAINT
ALTER TABLE usage_logs
	ADD CONSTRAINT uniq_constraint
	UNIQUE(logid);
--remove unique constraint
ALTER TABLE usage_logs
	DROP CONSTRAINT uniq_constraint

DROP TABLE usage_logs
--CHECK constraint at the table creation
CREATE TABLE usage_logs(
	logid INT NOT NULL UNIQUE CHECK (logid>10),
	message char(250)
	);
INSERT INTO usage_logs VALUES
(1,'test')
--The INSERT statement conflicted with the CHECK constraint "CK__usage_log__logid__59FA5E80". The conflict occurred in database "employee_db1", table "dbo.usage_logs", column 'logid'.
--The statement has been terminated.
INSERT INTO usage_logs VALUES
(11,'test')

--remove check constraint 
ALTER TABLE usage_logs
DROP CONSTRAINT CK__usage_log__logid__59FA5E80

INSERT INTO usage_logs VALUES
(1,'test')
--error is gone

SELECT * FROM usage_logs

--DEFAULT constraint on table creation
CREATE TABLE usage_logs(
	logid INT NOT NULL UNIQUE,
	message char(250),
	msgdate DATETIME NOT NULL DEFAULT GETDATE()
	);
INSERT INTO usage_logs VALUES
(1,'test')
--Column name or number of supplied values does not match table definition.
INSERT INTO usage_logs VALUES
(1,'test','')
--Not correct way eventhogh it showed output as
--1	test 1900-01-01 00:00:00.000
SELECT * FROM usage_logs

INSERT INTO usage_logs (logid,message) VALUES
(2,'test')
SELECT * FROM usage_logs
--1	test  1900-01-01 00:00:00.000
--2	test  2022-07-08 17:08:51.967

--add/remove constraint
ALTER TABLE usage_logs
	ADD CONSTRAINT def_date
	DEFAULT(GETDATE()) FOR msgdate;

ALTER TABLE usage_logs
	DROP CONSTRAINT def_date;