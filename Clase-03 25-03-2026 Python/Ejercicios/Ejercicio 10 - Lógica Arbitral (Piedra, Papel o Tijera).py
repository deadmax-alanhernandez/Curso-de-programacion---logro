print("Piedra, papel o tijera")

jugador1 = str(input("\n1er jugador (piedra, papel, o tijeras): ").lower())
jugador2 = str(input("\n2do jugador (piedra, papel, o tijeras): ").lower())

if jugador1 == "tijera" or jugador1 == "tijeras":
    if jugador2 == "papel":
        print(f"\nEl 1er jugador saco {jugador1} frente al {jugador2} del 2do jugador, gana el jugador 1!")
    elif jugador2 == "piedra" or jugador2 == "roca":
        print(f"\nEl 1er jugador saco {jugador1} frente a la {jugador2} del 2do jugador, gana el jugador 2!")
    elif jugador2 == "tijera" or jugador2 == "tijeras":
        print(f"\nEl 1er jugador saco {jugador1} pero el 2do jugador tambien saco {jugador2} , es un empate")
    else:
        print(f"\nLa jugada {jugador2} no es valida")

elif jugador1 == "papel":
    if jugador2 == "papel":
        print(f"\nEl 1er jugador saco {jugador1} pero el 2do jugador tambien saco {jugador2} del 2do jugador, es un empate")
    elif jugador2 == "piedra" or jugador2 == "roca":
        print(f"\nEl 1er jugador saco {jugador1} frente a la {jugador2} del 2do jugador, gana el jugador 1!")
    elif jugador2 == "tijera" or jugador2 == "tijeras":
        print(f"\nEl 1er jugador saco {jugador1} frente {jugador2} del 2do jugador, gane el jugador 2!")
    else:
        print(f"\nLa jugada del {jugador2} no es valida")

elif jugador1 == "piedra" or jugador1 == "roca":
    if jugador2 == "papel":
        print(f"\nEl 1er jugador saco {jugador1} frente al {jugador2} del 2do jugador, gana el jugador 2!")
    elif jugador2 == "piedra" or jugador2 == "roca":
        print(f"\nEl 1er jugador saco {jugador1} pero el 2do jugador tambien saco {jugador2}, es un empate")
    elif jugador2 == "tijera" or jugador2 == "tijeras":
        print(f"\nEl 1er jugador saco {jugador1} frente {jugador2} del 2do jugador, gana el jugador 1!")
    else:
        print(f"\nLa jugada del {jugador2} no es valida")

else:

    print(f"\nLa jugada {jugador1} no es valida")