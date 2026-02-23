create database project;
use project;
CREATE TABLE inventory ( id INT AUTO_INCREMENT PRIMARY KEY, veg_name VARCHAR(50) UNIQUE, quantity FLOAT, price INT,cost_price INT);
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50),phone BIGINT);
INSERT INTO inventory (veg_name, quantity, price, cost_price) VALUES
('brinjal',20,30,25),
('tomato',35,20,15),
('potato',35,35,30),
('ladiesfinger',15,25,20),
('drumsticks',10,40,30),
('bitterguard',10,35,30),
('spinach',8,15,12),
('onions',35,25,20),
('cabbage',10,35,30),
('cauliflower',10,30,25),
('capsicum',10,45,40);
select * from users;