print("Evaluador de contraseñas seguras")
print("\nLa longitud minima son 8 caracteres y la maxima 20")
print("\nDeben contener algun caracter especial")
tamano = (8, 20)
contrasenas = input("\nIngrese sus contraseñas, separelas con comas y sin espacios: ")
lista = contrasenas.split()
seguras = []

for it in lista:
    especial = False
    for letra in it:
        if not letra.isalnum():
            especial = True
            break
    if (len(it)) >= tamano[0] and (len(it)) <= tamano[1] and especial:
        seguras.append(it)
print(f"\nLas contraseñas seguras son: {seguras}")


