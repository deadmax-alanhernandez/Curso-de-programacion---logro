import random

class Personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
    def recibir_dano(self, recibido):
        self.salud -= recibido
        if self.salud < 0:
            self.salud = 0
        print(f"\n{self.nombre} recibio {recibido} de dano. Ahora tiene {self.salud} puntos de vida")


class Guerrero(Personaje):
    def ataque_pesado(self, objetivo):
        self.objetivo = objetivo
        dano_total = self.ataque
        print(f"\n---Ahora es turno de {self.nombre}---")
        if random.choice ([True, False]):
            if random.choice ([True, False]) == True:
                dano_total = self.ataque * 2
                print(f"\n{self.nombre} acierta un corte y realiza daño critico")
            else:
                print(f"\n{self.nombre} impacta un golpe efectivo")
        objetivo.recibir_dano(dano_total)

class Curandero(Personaje):
    def turno(self, objetivo):
        self.objetivo = objetivo
        print(f"\n---Ahora es turno de {self.nombre}---")
        
        if self.salud < 20:
            curacion = 35
            self.salud += curacion
            print(f"\n{self.nombre} uso tecnica inversa para curar sus heridas, recupera {curacion} de puntos de vida")
        else:
            print(f"\n{self.nombre} ataca con un golpe en el alma")
            objetivo.recibir_dano(self.ataque)

Yuji = Curandero ("Itadori", 100, 12)

Sukuna = Guerrero("Sukuna", 120, 14)

while Yuji.salud > 0 and Sukuna.salud > 0:
    Sukuna.ataque_pesado(Yuji)
    if Yuji.salud > 0:
        Yuji.turno(Sukuna)
if Sukuna.salud > 0: 
    print(f"\nSukuna acierta un ultimo corte que deja fuera de combate a yuji")
    print(f"\n(Expansión de Dominio: Santuario Malévolo) Sukuna expande su dominio y gana...")
else:
    print("\nItadori acierta un contundente BLACK FLASH")
    print("\nEl alma de sukuna se separa")
    print("\nItadori gana!!")



                

        
    