-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- CREATE DATA BASE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- TURN TO NEW DATA BASE
USE hbtn_0d_usa;
-- CREATE TABLE
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id));
