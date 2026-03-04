-- Group I - SEN CSC312 Lab Work (Web Application Development)
-- Ojo Abiola Victoria: MySQL table creation script — tbl_user for username and password storage.

CREATE DATABASE IF NOT EXISTS group1_lab_db;
USE group1_lab_db;

-- Table for user credentials (password column stores hashed password only)
CREATE TABLE IF NOT EXISTS tbl_user (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
