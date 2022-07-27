USE hospital_db

--create a new table
CREATE TABLE patient(
	patient_record_no INT IDENTITY PRIMARY KEY,
	patient_name VARCHAR(50),
	phone_number NUMERIC,
	--gender VARCHAR(10),
	age SMALLINT,
	location VARCHAR(50)
	);

--To alter an existing table
ALTER TABLE patient
	ADD gender VARCHAR(10);

--To descibe the details of the table
EXEC sp_help patient;

INSERT INTO patient
VALUES('Tina',9874561239,25, 'Mumbai','Female'),
('Sam',7874556239,35, 'Pune','Male'),
('Ken',8572656239,42, 'Leovale','Male');

--to fetch the data from the table
SELECT * FROM patient

--to update rows of data
UPDATE patient
SET patient_name = 'Preena'
WHERE patient_name = 'Tina';

--to fetch the data from the table
SELECT * FROM patient

--Delete a record from the table
DELETE FROM patient
WHERE patient_name = 'Preena'

--to fetch the data from the table
SELECT * FROM patient

--2	Sam	7874556239	35	Pune	Male
--3	Ken	8572656239	42	Leovale	Male
-- The number 1 is not updated becz the MSSQL is designed in such a way that the number once used cannot be reused again. Eventhough we have used autoincrement in the patientrecord set as primary key.