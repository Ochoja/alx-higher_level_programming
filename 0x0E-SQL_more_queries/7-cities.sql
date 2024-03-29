-- Creates a database and a table in the database
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select database
USE hbtn_0d_usa;
-- Create table in database
CREATE TABLE IF NOT EXISTS cities (
id INT NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states(id)
);
