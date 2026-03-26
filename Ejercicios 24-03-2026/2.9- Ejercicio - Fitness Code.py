print("Calculador del indice de masa corporal")

peso = float(input("Indique su peso en Kilogramos: "))
altura = float(input("indique su altura en metros: "))

print(f"El IMC es: {peso / (altura ** 2)}")