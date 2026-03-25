print("Verificacion de paridad")

num = int(input("Ingrese el numero: "))

resultado = num % 2

if resultado == 1 or resultado == -1:
    print(f"\nel numero {num} es impar")
    
elif resultado == 0:
    print(f"\nel numero {num} es par")