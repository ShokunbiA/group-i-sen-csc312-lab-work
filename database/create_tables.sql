-- Group I - SEN CSC312 Lab Work (Web Application Development)
--
-- Ojo Abiola Victoria: MySQL table creation script
-- Set up a MySQL database and create a table tbl_user to store user information
-- (username and password). Use this script to create the database and table before
-- running the Flask app. Run with: mysql -u root -p < database/create_tables.sql
--
-- Add your CREATE DATABASE, USE, and CREATE TABLE tbl_user statements below.
-- tbl_user should have columns for at least: id, username, password (and optionally created_at).
-- The password column will store the hashed password (hashing is done in app.py by Adeleke).

CREATE DATABASE IF NOT EXISTS group1_lab_db;
USE group1_lab_db;

CREATE TABLE IF NOT EXISTS tbl_user (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
