-- Create a database and user and grant SELECT privilege to user
-- Create database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
-- Create user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Set password of user user_0d_2
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
-- Grant user select privilege on database 'hbtn_0d_2'
GRANT SELECT ON 'hbtn_0d_2' TO 'user_0d_2'@'localhost';
