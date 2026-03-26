print("\nclasificacion de edad")

edad = int(input("\nIngrese su edad: "))

if edad >= 18 and edad < 120:
    print("\nusted es mayor de edad")

elif edad < 18 and edad > 0:
    print("\nusted es menor de edad")

else:
    print("\nError")
