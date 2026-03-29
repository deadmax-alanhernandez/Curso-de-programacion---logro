print("Validador de Calificaciones")
print("Minimo para pasar: 6.0 - Maximo para pasar: 10.0")
nota1 = float(input("\nIngrese la 1ra nota: "))
nota2 = float(input("\nIngrese la 2da nota: "))
nota3 = float(input("\nIngrese la 3ra nota: "))
nota4 = float(input("\nIngrese la 4ta nota: "))

lista = [nota1, nota2, nota3, nota4]
tupla = (6.0, 10.0)

for it in lista:
    if it >= tupla[0] and it <= tupla[1]:
        print(f"Tu calificacion es {it}, aprobaste! ")
    elif it < tupla[0] and it > 0:
        print(f"Tu calificacion es {it}, estas desaprobado")
    else:
        print(f"Error, valor no valido")