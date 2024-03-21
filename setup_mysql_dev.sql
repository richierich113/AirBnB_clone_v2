-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
