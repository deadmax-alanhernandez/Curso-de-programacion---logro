print("Filtrado de catalogo")
print("\nAqui podra observar una alta variedad de perifericos")

productos = [("Monitor Oled",129.99), 
             ("Teclado mecanico",30.50), 
             ("Mouse Logitech", 40.99), 
             ("Audifonos Ryzen", 80.00), 
             ("Adaptador HDMI", 9.99)]
lista = []
presupuesto = float(input("\nIngrese su presupuesto aqui: ")) 

for it in productos:
    if presupuesto >= it[1]:
        lista.append(it)
if presupuesto < 0:
    print(f"\nError, {presupuesto} no es un valor valido")
elif presupuesto >= it[1]:
    print("\nCon tu presupuesto te alcanza para:")
    print(lista)
else:
    print("\nLo siento, no te alcanza para ningun producto")
