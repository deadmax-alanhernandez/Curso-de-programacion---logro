print("\nAlgoritmo del Año Bisiesto")

fecha = int(input("\ningresa un año: "))

if (fecha % 4 == 0 and fecha % 100 != 0) or (fecha % 400 == 0):
    print(f"\n{fecha} es un año bisiesto")
    
else:
    print(f"\n{fecha} no es un año bisiesto")
    

