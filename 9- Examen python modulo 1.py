print("Conversor de Lista de Tuplas a diccionario")

lista = [("Nombre","Alan"), ("Edad", 17), ("Ciudad", "Maracaibo")]
diccionario = {}

resultado = dict(lista)

print(resultado)

#otra forma#

for id, valor in lista:
    diccionario[id] = valor

print(diccionario)