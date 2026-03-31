print("Elementos comunes en dos listas")
lista1 = [10, 12, 14, 16]
lista2 = [10, 11, 12, 13, 14]
def listas(lista1, lista2):
    compartida = []

    for digito in lista1:
        if digito in lista2 and digito not in compartida:
            compartida.append(digito)
    
    return compartida

print(f"Los elementos comunes son: {listas(lista1, lista2)}")