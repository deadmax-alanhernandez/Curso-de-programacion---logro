print("Simulador de Duelos!!")

print("Bienvenido a la Arena!, lucha con todo lo que tengas contra otro gladiador")

hp = [100, 100]

posibles = (5, 10, 20, 30)
 
while hp[0] > 0 and hp[1] > 0:
    print(f"\nVida actual:{hp[0]}")
    print(f"\nVida del enemigo:{hp[1]}")
    print(f"\n--Empieza tu turno--")
    print("\nSelecciona un ataque")
    print("--Patada--")
    print("--Golpe--")
    print("--Tajo--")
    print("--Apuñalar--")
    
    ataque = input("--> ")
    if ataque.lower() == "patada":
        hp[1] -= posibles[1]
        print(f"\nTu patada conecta, y le haces un total de {posibles[1]} de daño")
    elif ataque.lower() == "golpe":
        hp[1] -= posibles[0]
        print(f"\nTu golpe conecta... pero casi no traspasa la armadura")
        print(f"\nHiciste un total de {posibles[0]} de daño")
    elif ataque.lower() == "tajo":
        hp[1] -= posibles[2]
        print(f"\nRealizas un tajo con la espada que conecta con tu oponente!")
        print(f"\nHiciste un total de {posibles[2]} de daño")
    elif ataque.lower() == "apuñalar":
        hp[1] -= posibles[3]
        print(f"\nIncreible! Tu puñalada hizo un daño devastador, tu oponente se retuerce")
        print(f"\nHiciste un total de {posibles[3]} de daño")
    else:
        print("\nAtaque no valido, perdiste un turno")
    
    if hp[1] <= 0:
        break
    
    print("\nLa tecnica del gladiador es firme, te hace un total de 20 de daño")
    hp[0] -= 20

print("---¡Fin del combate!----")

if hp[0] <= 0:
    print("\nHas sido derrotado, te pones de rodillas en la arena ya moribundo y aceptas tu destino.")
    print("\nGAME OVER")

else:
    print("\nVICTORIA")
    print("\nFuiste el vencedor del combate, y ahora eres el campeon de la arena")
    


    
    
