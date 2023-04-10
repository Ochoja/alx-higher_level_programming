-- Creates user and grants user privileges
-- Creates user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Set password for above user
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
-- Grant user permissions
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
