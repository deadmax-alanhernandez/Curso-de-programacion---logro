CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  name VARCHAR(150), price int, stock int);



ALTER TABLE Products 
ADD COLUMN category VARCHAR (100)


ALTER TABLE Products
MODIFY COLUMN name VARCHAR(255)

CREATE TABLE Customers (customer_id INT PRIMARY KEY,
first_name VARCHAR(120), last_name VARCHAR(120), age int, country VARCHAR(100), email VARCHAR(200))


INSERT INTO Customers (customer_id, first_name, last_name, age, country, email) VALUES
(1, 'Juan', 'Perez', 28, 'Mexico', 'juan.perez@email.com'),
(2, 'Ana', 'García', 34, 'España', 'ana.garcia@email.com'),
(3, 'Carlos', 'Rodriguez', 45, 'Argentina', 'carlos.r@email.com'),
(4, 'Maria', 'Lopez', 22, 'Colombia', 'maria.lopez@email.com'),
(5, 'Luis', 'Martinez', 52, 'Mexico', 'luis.martinez@email.com');


INSERT INTO Products (product_id, name, price, stock, category) VALUES
(101, "Jabon de tocador", 0.65, 20, "Cuidado personal"),
(102, "Polvo compacto", 1.50, 6, "Maquillaje"),
(103, "Toallas sanitarias", 1.00, 14, "Cuidado personal"),
(104, "Ibuprofeno 100gr", 7.40, 4, "Medicina"),
(105, "Acetaminofen 60gr", 6.80, 7, "Medicina");


UPDATE Customers set country = "España" WHERE first_name = "Juan"