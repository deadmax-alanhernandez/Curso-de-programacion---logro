print("Carrito de compras")

productos = []
precios = []
print("¡Bienvenido!")
print("Que deseas hacer?")

while True:
    print("----MENU----")
    print("1.- AGREGAR ELEMENTO")
    print("2.- MOSTRAR CARRITO")
    print("3.- ELIMINAR ELEMENTO")
    print("4.- CALCULAR TOTAL")
    print("5.- RENUNCIAR (SALIR)")

    elegir = (input("Seleccione una opcion (1-5): "))

    if elegir == "1":
        nombre = input("Ingrese el nombre del producto: ").capitalize()
        precio = float(input("Ingrese el precio del producto: "))
        if precio > 0: 
            productos.append(nombre)
            precios.append(precio)
            print(f"el producto {nombre} fue añadido al carrito")
        else:
            print("Precio no valido, intente de nuevo")
    elif elegir == "2":
        if len(productos) == 0:
            print("Tu carrito esta vacio")
        else:
            print("---CONTENIDO DEL CARRITO-----")
            for it in range(len(productos)):
                print(f"{it + 1}. {productos[it]} : {precios[it]}") 
    elif elegir == "3":
        if len(productos) == 0:
            print("Tu carrito esta vacio")
        else:
            for it in range (len(productos)):
                print(f"{it + 1}. {productos[it]} : {precios[it]}")
            eliminar = int(input("Introduce el numero del producto que deseas eliminar: "))
            real = eliminar - 1
            if real >= 0 and real < len(productos):
                eliminado = productos.pop(real)
                precios.pop(real)   
                print(f"Se ha descartado el producto {eliminado}")
            else:
                print("Valor no valido")
    elif elegir == "4":
        total = 0
        for suma in precios:
            total += suma
        print(f"\n El total de tu compra es: {total}")
    elif elegir == "5":
        print("Entendido, hasta luego!")
        break
    else:
        print("Opcion invalida, intenta nuevamente")



    
    

