CREATE DATABASE IF NOT EXISTS ECommerceDB;

USE ECommerceDB;

CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  name VARCHAR(150), price int, stock int);



ALTER TABLE Products 
ADD COLUMN category VARCHAR (100);


ALTER TABLE Products
MODIFY COLUMN name VARCHAR(255);

CREATE TABLE Customers (customer_id INT PRIMARY KEY,
first_name VARCHAR(120), last_name VARCHAR(120), age int, country VARCHAR(100), email VARCHAR(200));

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    item VARCHAR(100),
    amount INT,
    customer_id INT 
);


CREATE TABLE Shippings (
    shipping_id INT PRIMARY KEY,
    status VARCHAR(100),
    customer_id INT 
);

INSERT INTO Orders (order_id, item, amount, customer_id) VALUES
(101, 'Laptop', 1, 1),
(102, 'Mouse', 2, 1),
(103, 'Teclado', 1, 2),
(104, 'Monitor', 1, 3),
(105, 'Webcam', 1, 4),
(106, 'Mouse', 1, 4),
(107, 'Laptop', 1, 5);

INSERT INTO Shippings (shipping_id, status, customer_id) VALUES
(201, 'Shipped', 1),
(202, 'Pending', 2),
(203, 'Delivered', 3),
(204, 'Shipped', 4);

INSERT INTO Customers (customer_id, first_name, last_name, age, country, email) VALUES
(1, 'Juan', 'Perez', 28, 'Mexico', 'juan.perez@email.com'),
(2, 'Ana', 'García', 34, 'España', 'ana.garcia@email.com'),
(3, 'Carlos', 'Rodriguez', 45, 'Argentina', 'carlos.r@email.com'),
(4, 'Maria', 'Lopez', 22, 'Colombia', 'maria.lopez@email.com'),
(5, 'Luis', 'Martinez', 52, 'Mexico', 'luis.martinez@email.com');


INSERT INTO Products (product_id, name, price, stock, category) VALUES
(1, 'Laptop', 1200, 10, 'Electronica'),
(2, 'Mouse', 25, 50, 'Perifericos'),
(3, 'Teclado', 80, 15, 'Perifericos'),
(4, 'Silla Oficina', 200, 5, 'Muebles'),
(5, 'Escritorio L', 350, 8, 'Muebles'),
(6, 'Monitor', 150, 6, 'Perifericos'),
(7, 'Webcam', 80, 7, 'Perifericos');


UPDATE Customers set country = "España" WHERE first_name = "Juan" or customer_id = 4

DELETE FROM Shippings WHERE status = 'Delivered' AND shipping_id > 200;

SELECT * FROM Customers WHERE age > 30 AND country NOT IN ('Mexico', 'Colombia');

SELECT name, price, stock FROM Products ORDER BY stock DESC, price ASC;

SELECT SUM(amount) FROM Orders WHERE amount >= 2;

SELECT MAX(age), MIN(age) FROM Customers;

SELECT COUNT(*) FROM Orders WHERE customer_id IN (1, 3, 5);