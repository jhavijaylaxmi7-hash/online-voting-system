CREATE DATABASE voting_db;
USE voting_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    otp VARCHAR(10),
    is_verified BOOLEAN DEFAULT FALSE
);

CREATE TABLE votes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    candidate VARCHAR(50)
);