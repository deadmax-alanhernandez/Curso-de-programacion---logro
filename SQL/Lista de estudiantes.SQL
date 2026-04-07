CREATE TABLE Estudiantes (
  cedula INT PRIMARY KEY,
  nombre varchar(50),
  segundo_nombre varchar(50),
  apellido varchar(50),
  correo varchar(100),
  edad int,
  pelicula_fav varchar (100));
  
  insert into Estudiantes (cedula, nombre, segundo_nombre, apellido, correo, edad, pelicula_fav) VALUES
  (33104854, "Alan", "David", "Hernandez", "alan.hernandez3310@gmail.com", 17, "Spiderman: a través del multiverso"),
  (31989067, "Adrian", "Jesus", "Vera", "abokase4706@gmail.com", 20, "Avengers"),
  (31096641, "Jose", "Angel", "Franco", "josefranber2609@gmail.com", 21, "Rey leon"),
   (32577415, "Javier", "Alejandro", "Medina", "No data", 17, "Thor");


