nombres = ["Alice", "Bob", "Charlie", "David", "Eve"]

print(f"nombres: {nombres}")
print(f"nombre: {nombres}[-1]")

nombres[2] = "Espitia"
print(f"\nNombres despues de la modificiacion {nombres}")

nombres.append("Frank")
print(f"\nNombres despues de la modificiacion {nombres}")

nombres.insert(1, "Grace")
print(f"\nNombres despues de la modificiacion {nombres}")

nombres.remove("Bob")
print(f"\nNombres despues de la modificiacion {nombres}") 

nombres.pop(3)
print(f"\nNombres despues de la modificiacion {nombres}")

del nombres[0]
print(f"\nNombres despues de la modificiacion {nombres}")

