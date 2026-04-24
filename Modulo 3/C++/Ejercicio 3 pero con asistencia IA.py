import random

class Personaje:
    def __init__(self, nombre, salud, ataque, energia_maldita):
        self.nombre = nombre
        self.salud_max = salud
        self.salud = salud
        self.ataque_base = ataque
        self.energia_maldita = energia_maldita

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0
        print(f"[{self.nombre}] recibe {dano} de daño. (Salud restante: {self.salud}/{self.salud_max})")

    def esta_vivo(self):
        return self.salud > 0

class Yuji(Personaje):
    def turno(self, objetivo):
        print(f"\n{'='*40}")
        print(f"Turno de {self.nombre} | PV: {self.salud}/{self.salud_max} | EM: {self.energia_maldita}")
        print("¿Qué harás?")
        print("a) Puño Divergente (Ataque Básico)")
        print("b) Desmantelar del Alma (Coste: 15 EM)")
        print("c) Manipulación de Sangre: Convergencia (Coste: 20 EM)")
        print("d) Técnica Inversa (Curar, Coste: 30 EM)")
        
        # Validamos el input como string para evitar el uso de enteros
        opcion = ""
        while opcion not in ["a", "b", "c", "d"]:
            opcion = input("Elige tu acción (a/b/c/d): ").lower()

        dano_total = 0
        
        if opcion == "a":
            dano_total = self.ataque_base
            print(f"\n{self.nombre} ataca con Puño Divergente.")
        
        elif opcion == "b":
            if self.energia_maldita >= 15:
                self.energia_maldita -= 15
                dano_total = self.ataque_base * 1.5
                print(f"\n{self.nombre} usa la Técnica Ritual de Sukuna: ¡Desmantelar del Alma!")
            else:
                print("\nNo hay suficiente Energía Maldita. Atacas con un golpe normal.")
                dano_total = self.ataque_base
                
        elif opcion == "c":
            if self.energia_maldita >= 20:
                self.energia_maldita -= 20
                dano_total = self.ataque_base * 2
                print(f"\n{self.nombre} comprime su sangre: ¡Sangre Perforante!")
            else:
                print("\nNo hay suficiente Energía Maldita. Atacas con un golpe normal.")
                dano_total = self.ataque_base

        elif opcion == "d":
            if self.energia_maldita >= 30:
                self.energia_maldita -= 30
                curacion = 150
                self.salud = min(self.salud_max, self.salud + curacion)
                print(f"\n{self.nombre} usa Técnica Inversa. Recupera {curacion} PV.")
            else:
                print("\nNo hay suficiente EM para curarse. Pierdes el turno por la fatiga.")
        
        # Mecánica del Black Flash (Destello Negro)
        if dano_total > 0:
            probabilidad_black_flash = random.randint(1, 100)
            if probabilidad_black_flash <= 25: # 25% de probabilidad de Black Flash
                dano_total = int(dano_total * 2.5)
                print("\n¡Las chispas negras no eligen a quién bendecir!")
                print(f"¡{self.nombre} conecta un DESTELLO NEGRO (BLACK FLASH)!")
            
            objetivo.recibir_dano(int(dano_total))

class Sukuna(Personaje):
    def __init__(self, nombre, salud, ataque, energia_maldita):
        super().__init__(nombre, salud, ataque, energia_maldita)
        self.voto_vinculante_activo = False

    def turno(self, objetivo):
        print(f"\n{'='*40}")
        print(f"Turno de {self.nombre} | PV: {self.salud}/{self.salud_max}")
        
        if self.voto_vinculante_activo:
            print("\nSukuna ha completado los cánticos de su Voto Vinculante...")
            print("¡CORTE QUE PARTE EL MUNDO (World Cutting Slash)!")
            dano = self.ataque_base * 3.5
            objetivo.recibir_dano(int(dano))
            self.voto_vinculante_activo = False
            return

        eleccion = random.choice(["desmantelar", "partir", "voto_vinculante"])
        
        if eleccion == "desmantelar":
            dano = self.ataque_base
            print(f"\n{self.nombre} lanza una ráfaga de cortes: Desmantelar.")
            objetivo.recibir_dano(int(dano))
            
        elif eleccion == "partir":
            dano = self.ataque_base * 1.5
            print(f"\n{self.nombre} toca a su objetivo: Cleave (Partir).")
            objetivo.recibir_dano(int(dano))
            
        elif eleccion == "voto_vinculante":
            print(f"\n{self.nombre} sonríe y junta sus manos... 'Escama de Dragón, Repulsión, Meteoros Gemelos'.")
            print("Sukuna sacrifica su turno actual para establecer un VOTO VINCULANTE y potenciar su próximo ataque.")
            self.voto_vinculante_activo = True

def asistencia_aliada(objetivo_enemigo):
    # 30% de probabilidad de que un aliado intervenga al inicio de un turno
    if random.randint(1, 100) <= 70:
        aliados = ["Aoi Todo", "Maki Zenin", "Yuta Okkotsu", "Choso"]
        aliado_actual = random.choice(aliados)
        
        print(f"\n>>> ¡APARICIÓN REPENTINA! <<<")
        if aliado_actual == "Aoi Todo":
            print("Todo hace sonar su Vibraslap. ¡Boogie Woogie!")
            print("Cambia la posición de Sukuna, dejándolo vulnerable para el ataque.")
            return 1.5 # Multiplicador de daño para el turno de Yuji
        elif aliado_actual == "Maki Zenin":
            print("Maki aparece desde un punto ciego y ataca con la Katana que Separa el Alma.")
            dano_aliado = 80
            objetivo_enemigo.recibir_dano(dano_aliado)
        elif aliado_actual == "Yuta Okkotsu":
            print("Yuta materializa a Rika parcialmente, inmovilizando a Sukuna por un instante.")
            dano_aliado = 60
            objetivo_enemigo.recibir_dano(dano_aliado)
        elif aliado_actual == "Choso":
            print("¡Choso dispara Supernova! '¡No tocarás a mi hermano!'")
            dano_aliado = 50
            objetivo_enemigo.recibir_dano(dano_aliado)
    return 1.0 # Multiplicador normal si no hay ventaja de Todo

# === CONFIGURACIÓN DE LA BATALLA ===
# Balance de estadísticas para que sea desafiante pero ganable
itadori = Yuji("Itadori Yuji", salud=500, ataque=40, energia_maldita=100)
sukuna = Sukuna("Ryomen Sukuna", salud=800, ataque=65, energia_maldita=500)

print("¡COMIENZA EL COMBATE FINAL EN SHINJUKU!")

while itadori.esta_vivo() and sukuna.esta_vivo():
    # Input para pausar el código y que no corra de golpe
    input("\n[Presiona Enter para continuar al siguiente turno...]")
    
    # Asistencia antes del turno de Yuji
    multiplicador_ventaja = asistencia_aliada(sukuna)
    
    if not sukuna.esta_vivo():
        break # Por si la asistencia aliada mata a Sukuna

    # Turno del jugador
    itadori.turno(sukuna)
    
    # Aplicar ventaja temporal de Todo si la hubo (lógica simplificada para el ejemplo)
    if multiplicador_ventaja > 1.0:
        print("(El ataque de Yuji fue más efectivo gracias a Todo)")
    
    if not sukuna.esta_vivo():
        break
        
    input("\n[Presiona Enter para el turno del enemigo...]")
    
    # Turno del jefe
    sukuna.turno(itadori)

# === RESULTADOS DE LA BATALLA ===
print("\n" + "="*40)
if sukuna.esta_vivo():
    print(f"\n(Expansión de Dominio: Santuario Malévolo)")
    print("Sukuna expande su dominio definitivo. Yuji cae en combate...")
    print("EL REY DE LAS MALDICIONES GANA.")
else:
    print("\n¡Itadori acierta un último y contundente BLACK FLASH!")
    print("¡El alma de Megumi es liberada y Sukuna se separa!")
    print("¡ITADORI YUJI GANA LA BATALLA DE SHINJUKU!")