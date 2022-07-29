USE Camp2
CREATE TABLE stations(
	station_id INT PRIMARY KEY,
	station_name VARCHAR(20)
	);

CREATE TABLE trains(
	train_id INT IDENTITY PRIMARY KEY, 
	train_name VARCHAR(20),
	start_name VARCHAR(20),
	dest_name VARCHAR(20),
	stop_id INT FOREIGN KEY REFERENCES stations(station_id),
	berth_fill INT,
	wait_list_fill INT
);
CREATE TABLE passengers(
	passenger_id INT IDENTITY PRIMARY KEY,
	passenger_name VARCHAR(20),
	station_id INT FOREIGN KEY REFERENCES stations(station_id),
	train_id INT FOREIGN KEY REFERENCES trains(train_id)
);
CREATE TABLE waitlist(
	passenger_id INT IDENTITY PRIMARY KEY,
	passenger_name VARCHAR(20),
	station_id INT FOREIGN KEY REFERENCES stations(station_id),
	train_id INT FOREIGN KEY REFERENCES trains(train_id)
)
INSERT INTO stations VALUES 
(0,'TVM'),
(1,'ALP'),
(2,'ERN'),
(3,'KZK');

INSERT INTO trains VALUES
('TVM_ALP','TVM','ALP',1,0,0),
('TVM_ERN','TVM','ERN',2,0,0),
('TVM_KZK','TVM','KZK',3,0,0);

SELECT * FROM stations
SELECT * FROM trains
SELECT * FROM passengers
SELECT * FROM waitlist
--DROP TABLE stations
--DROP TABLE trains
--DROP TABLE passengers
--DROP TABLE waitlist