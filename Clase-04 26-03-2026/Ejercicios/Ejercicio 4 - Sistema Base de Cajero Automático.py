print("Cajero Automatico")
print("Bienvenido ¿Que deseas hacer?")
opciones = ("1", "2", "3", "4")
saldo = 250
historial = []
intentos = []

while True:
    print("1 -- Consultar")
    print("2 -- Depositar")
    print("3 -- Retirar")
    print("4 -- Salir")
    decision = int(input("\nSelecciona un comando (1-4) --> "))
    if decision < 1 or decision > 4:
         print(f"\n{decision} no es un comando valido, intente de nuevo")
         intentos.append(decision)
         print(f"\nintentos fallidos: {intentos}")
    elif decision == 1:
         print(f"\nSu Saldo es de {saldo} dolares")
         historial.append(decision)
    elif decision == 2:
         historial.append(decision)
         deposito = float(input("\n¿Cuanto desea depositar?: "))
         if deposito > 0:
              saldo += deposito
              print(f"\nExcelente! ahora su saldo actual es de {saldo} ")
              historial.append(deposito)
         else:
              print(f"\nError, intente de nuevo")
              intentos.append(deposito)
        
    elif decision == 3:
         retiro = float(input("\n¿Cuanto desea retirar?: "))

         if retiro < 0 or retiro <= saldo:
             saldo -= retiro
             print(f"\nExcelente! ha retirado {retiro} y ahora su actual es de {saldo}")
             historial.append(retiro)
         else:
              print(f"\nError, intente de nuevo")
              intentos.append(retiro)
    elif decision == 4:
         print("\nBien, Hasta luego!")
         break
print(f"\nHistorial: {historial}")

