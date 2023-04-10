-- Creates a database and a table in the database
-- Create hbtn_0d_usa Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select Database
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);
