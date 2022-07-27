USE Camp2
CREATE TABLE stations(
	station_id INT PRIMARY KEY,
	station_name VARCHAR(20)
	);

CREATE TABLE trains(
	train_id INT PRIMARY KEY, 
	train_name VARCHAR(20),
	start_name VARCHAR(20),
	dest_name VARCHAR(20),
	stop_id INT FOREIGN KEY REFERENCES stations(station_id),
	berth_no INT,
	wait_list INT
);
CREATE TABLE passengers(
	passenger_id INT PRIMARY KEY,
	passenger_name VARCHAR,
	dest_name VARCHAR(20)
);
INSERT INTO stations VALUES 
(0,'TVM'),
(1,'ALP'),
(2,'ERN'),
(3,'KZK');

INSERT INTO trains VALUES
(1,'TVM_ALP','TVM','ALP',1,5,2),
(2,'TVM_ERN','TVM','ERN',2,5,2),
(3,'TVM_KZK','TVM','KZK',3,5,2);

