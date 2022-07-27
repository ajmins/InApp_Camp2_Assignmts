--To create a new database
CREATE DATABASE employee_db1

--List all databases in the server
SELECT name from master.sys.databases;

--List all databases in the server order by name
SELECT name from master.sys.databases ORDER BY name;

--Select the databse
USE employee_db1

--To create the backup of database
BACKUP DATABASE emplyoee_db1 TO DISK = 'J:\sql_bckp\employee_db1.bak'
--Processed 344 pages for database 'employee_db1', file 'employee_db1' on file 1.
--Processed 2 pages for database 'employee_db1', file 'employee_db1_log' on file 1.
--BACKUP DATABASE successfully processed 346 pages in 0.236 seconds (11.437 MB/sec).

--To create the backup of database
BACKUP DATABASE emplyoee_db1 TO DISK = 'D:\database_backup\employee_db1.bak' WITH DIFFERENTIAL

USE master
--delete database
DROP DATABASE emplyoee_db1

--restoring data from the backup
RESTORE DATABASE emplyoee_db1
FROM DISK = 'D:\database_backup\employee_db1.bak'
WITH REPLACE

--Select the databse
USE emplyoee_db1

--find the default schema of the current database
SELECT SCHEMA_NAME()

--create a new schema 
CREATE SCHEMA myschema1

--create a new schema by xplictly specifying the user
CREATE SCHEMA myschema2 AUTHORIZATION dbo

--create a table and placing it under the myschema1 schema
CREATE TABLE myschema1.mytable1(
ID int,
FirstName nvarchar(50) NOT NULL,
LastName nvarchar(50) NOT NULL
);

--Remove the database schema from the database
DROP SCHEMA IF EXISTS myschema1
--error: Cannot drop schema 'myschema1' because it is being referenced by object 'mytable1'.

--so transfer/change all the db object (eg:table) into another schema
ALTER SCHEMA dbo 
TRANSFER OBJECT::myschema1.mytable1

--Remove the database schema from the database
DROP SCHEMA IF EXISTS myschema1