class estudiante:
    #Atributos de clase
    universidad = "Ninguna"

    def __init__(self, nombre, carrera, cedula, edad):
        self.nombre = nombre
        self.carrera = carrera
        self.cedula = cedula
        self.edad = edad
    
    def estudiar(self, estudio):
        estudio = input("Estas estudiando (si/no)")
        
        if estudio.lower() == "si":
            print("Sigue estudiando")
        else:
            print("Deberias estudiar mas")

class trabajo:
    
    empresa = "Ninguna"
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def cobrar(self):
        empresa = input("En que empresa trabajas?: ")
        if empresa.lower() == "ninguna":
            print("no tienes trabajo")
        elif empresa.lower()== "google":
            cobro = input("Ya cobraste?: ")
            if cobro.lower() == "si":
                print("Disfruta tu dinero")
            else:
                print("Que triste")
        else:
            print("Error entrada no valida")       

        



persona1 = estudiante("Alan", "Telecomunicaciones", "33104854", "17")
trabajador1 = trabajo("Alan", "Soporte TI" )

persona1.estudiar("no")
trabajo.cobrar()