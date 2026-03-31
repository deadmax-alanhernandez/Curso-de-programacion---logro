print("Agenda de contactos")
print("\nBienvenido, que desea hacer?")
agenda = {}
while True:
    print("\n1 -- Incluir contacto")
    print("2 -- Buscar un contacto")
    print("3 -- Listar todos los contactos")
    print("4 -- Salir")
    decision = int(input("\nSelecciona un comando (1-4) --> "))
    if decision < 1 or decision > 4:
         print(f"\n{decision} no es un comando valido, intente de nuevo")
         
    elif decision == 1:
         nombre = input("\nIntroduce el nombre del nuevo contacto: ").strip().capitalize()
         numero = input("\nIntroduce el numero del nuevo contacto: ")
         
         agenda[nombre] = numero
         print("\nSu contacto ha sido añadido")
    elif decision == 2:
         
         buscar = input("\n¿A quien deseas buscar?: ").strip().capitalize()
         if buscar in agenda:
              print(f"\nEl numero de {buscar} es: {agenda[buscar]}")
         elif len(agenda) == 0:
             print("\nLa agenda no tiene ningun contacto guardado")
         else:
              print(f"\nEl contacto {buscar} no esta en la agenda")
              
        
    elif decision == 3:
        if len(agenda) == 0:
            print("\nLa agenda no tiene ningun contacto guardado")
        elif len(agenda) > 0:
             print("\nLista de contactos")
             for nombres, tele in agenda.items():
                  print(f"\n{len(agenda)}.- {nombres} --- {tele}")
        else:
            print(f"\nError, intente de nuevo")
              
    elif decision == 4:
         print("\nBien, Hasta luego!")
         break