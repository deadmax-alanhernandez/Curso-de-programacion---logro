print("Calculadora de promedio")

lista = []
print("Creara una lista de numeros, cuando haya completado su lista ingrese (FIN)")
while True:
    numero = float(input("Ingrese un numero: "))
    if numero > 0:
        lista.append(numero)
        continuar = input("Desea continuar? (FIN/SI): ").upper()
        if continuar == "FIN":
            break
        elif continuar == "SI":
            print("Continuemos")
            print(f"Lista: {lista}")
        else:
            print("Ingrese una opcion valida")
    else:
        print("Ingrese un numero valido")

suma = 0
division = 0

for calculo in lista:
    suma+= calculo
    division+= 1

if division > 0:
    print(f"El promedio de estos numeros es: {suma / division}")
else:
    print("No hay datos con que trabajar")
    
