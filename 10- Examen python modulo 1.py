print("Triangulo de astericos")

cantidad = int(input("ingrese el numero de niveles que quiere en su triangulo: "))

for asterico in range(1, cantidad + 1):
    print(f"*" * asterico)