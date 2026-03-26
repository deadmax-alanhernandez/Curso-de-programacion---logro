print("Categorizacion de Triangulos")

lado1 = float(input("\nprimer lado: "))
lado2 = float(input("\nsegundo lado: "))
lado3 = float(input("\ntercer lado: "))


if (lado1 + lado2) >lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print("\nEfectivamente, es un triangulo")
    if lado1 == lado2 == lado3:
        print("su triangulo es un triangulo equilatero")
    
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2:
        print("su triangulo es un triangulo isosceles")
    else:
        print("su triangulo es un triangulo escaleno")


else:
    print("No califica como triangulo")

