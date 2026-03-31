print("Frecuencia de palabras en un texto")
frecuencia = {}

parrafo = input("Introce un texto: ")

separacion = parrafo.lower().split()

for palabra in separacion:
    if palabra in frecuencia:
        frecuencia[palabra] +=1
    else:
        frecuencia[palabra] = 1

print("Las palabras se repiten esta cantidad de veces: ")
print(frecuencia)
