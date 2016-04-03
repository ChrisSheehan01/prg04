#Chris Sheehan & Dan "The Man's" Howard
#April 3, 2016
#Programming Assignment 4

DROP DATABASE IF EXISTS prg04;

#Creates a Database called "prg04"
CREATE DATABASE prg04;

#Chooses the Database "prg04" as the Database to use
USE prg04;

#Part I - Data Model
#Creates the table Users 
#	with id as the primary key
CREATE TABLE Users(
id INT NOT NULL,
name VARCHAR(15) NOT NULL,
PRIMARY KEY (id)
);

#Creates the table Rooms
#	with build and number as the primary key
CREATE TABLE Rooms(
build VARCHAR(10) NOT NULL,
number INT NOT NULL,
PRIMARY KEY (build, number)
);

#Creates the table ReservedRooms
#	with seq as the primary key
CREATE TABLE Reserved_Rooms(
seq INT NOT NULL,
date DATE,
begin INT,
end INT,
user_id INT,
build VARCHAR(10),
roomNum INT,
FOREIGN KEY (user_id) REFERENCES Users (id),
#impossible
#FOREIGN KEY (roomNum) REFERENCES Rooms (number),
FOREIGN KEY (build) REFERENCES Rooms (build),
PRIMARY KEY (seq)
);

#Inserts the following tuples into the Users table
INSERT INTO Users VALUES
(1, "John"),
(2, "Mary");

#Inserts the following tuples into the Rooms table
INSERT INTO Rooms VALUES
("CHS", 110),
("PPHAC", 113),
("PPHAC", 114);

#Inserts the following tuples into the Reserved_Rooms table
INSERT INTO Reserved_Rooms VALUES
#both ways of inputting date are wrong
(1, "2016-03-20", 08, 09, 1, "PPHAC", 113),
(2, "2016-04-01", 08, 10, 2, "PPHAC", 114);

#Creates View, ReservationsView
#	Lists all reservations and user names
CREATE VIEW ReservationsView AS
	SELECT
		rr.seq AS number,
		CONCAT(rr.build,'-',rr.roomNum) AS room,
		rr.date,
		CONCAT(rr.begin,'-',rr.end) AS time,
		CONCAT(u.id,'-',u.name) AS user
	FROM
		Reserved_Rooms rr
			INNER JOIN
		Users u ON rr.user_id = u.id
	ORDER BY
		rr.seq ASC;


#Part 2 - Room Reservation System
#prg04.py
