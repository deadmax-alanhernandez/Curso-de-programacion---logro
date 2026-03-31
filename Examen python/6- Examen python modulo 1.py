print("Suma de numeros pares")

numeros = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

suma = 0

for cantidad in numeros:
    if cantidad % 2 == 0:
        suma += cantidad

print(f"El total de la suma entre los numeros pare es: {suma}")