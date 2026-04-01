print("¿Cual es mas larga?")

palabra1 = str(input("ingrese palabra 1: "))
palabra2 = str(input("ingrese palabra 2: "))

largo = len(palabra1) > len(palabra2)

print(f"¿{palabra1} es mas larga que palabra {palabra2}?")
print(largo)