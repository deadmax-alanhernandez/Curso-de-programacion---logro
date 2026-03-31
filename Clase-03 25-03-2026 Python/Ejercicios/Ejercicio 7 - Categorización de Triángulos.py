print("Categorizacion de Triangulos")

lado1 = float(input("\nasigne el valor del primer lado: "))
lado2 = float(input("\nasigne el valor del segundo lado: "))
lado3 = float(input("\nasigne el valor del tercer lado: "))


if (lado1 + lado2) >lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print("\nEfectivamente, es un triangulo")
    if lado1 == lado2 == lado3:
        print("\ny su triangulo es un triangulo equilatero")
    
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2:
        print("\ny su triangulo es un triangulo isosceles")
    else:
        print("\ny su triangulo es un triangulo escaleno")


else:
    print("\nNo califica como triangulo")

