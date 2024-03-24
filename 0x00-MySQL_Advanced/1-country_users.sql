-- create table, user with basic requirements


CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country enum('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
