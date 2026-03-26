print("\nsistema de descuentos")

precio = float(input("\nPrecio del producto: "))

if precio >= 1000:
    print(f"\nSu producto recibe un descuento del 15%, el precio total es: {precio - (precio * 0.15)} dolares")

elif precio < 1000 and precio > 0:
    print(f"\nEl producto no figura en el descuento")

else:
    print("\nError")