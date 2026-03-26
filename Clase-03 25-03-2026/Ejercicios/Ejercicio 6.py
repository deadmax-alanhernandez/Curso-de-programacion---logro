print("Calculadora Aritmetica Basica")

num1 = float(input("\nprimer numero: "))
operador = input("\neliga su operador (+,-,x,/): ").lower()
num2 = float(input("\nSegundo numero: "))

if operador == "+":
    print(f"\n{num1 + num2}")

elif operador == "-":
    print(f"\n{num1 - num2}")

elif operador == "*" or operador == "x" or operador == ".":
    print(f"\n{num1 * num2}")

elif operador == "/": 
    if num2 != 0:
        print(f"\n{num1 / num2}")
    else:
        print("\nError, no puedes dividir entre cero jaja")

else:
    print("\nNumero o Operador no valido")
