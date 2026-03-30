import random
print("Adivina el Numero")

print("Bienvenido al juego")

numero = random.randint(1, 101)

while True:
    adivinar = int(input("Puedes adivinar el numero del 1 al 100?: "))
    if adivinar == numero:
        print("Felicidades, has adivinado!")
    elif adivinar < numero:
        print("Te equivocaste, pero te doy una pista")
        print("Tu numero es menor al mio")
    elif adivinar > numero:
        print("Te equivocaste, pero te doy una pista")
        print("Tu numero es mayor al mio")      
    else:
        print("ERROR")  