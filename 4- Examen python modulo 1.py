print("Verificador de palindromos")

def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")

    vuelta = palabra[::-1]
    if palabra == vuelta:
        return True
    else:
        return False

respuesta = input("Introduzca una palabra o frase: ")

resultado = palindromo(respuesta)

if resultado:
    print(f"{respuesta} es un palindromo")
else:
    print(f"{respuesta} no es un palindromo")