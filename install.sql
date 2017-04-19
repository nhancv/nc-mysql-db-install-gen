CREATE USER IF NOT EXISTS 'DB_USER'@'DB_HOST' IDENTIFIED BY 'DB_PASSWORD';
DROP DATABASE IF EXISTS DB_NAME;
CREATE DATABASE IF NOT EXISTS DB_NAME CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE DB_NAME;
GRANT ALL PRIVILEGES ON DB_NAME.* TO DB_USER@DB_HOST;
SOURCE ./DB_NAME.sql;
