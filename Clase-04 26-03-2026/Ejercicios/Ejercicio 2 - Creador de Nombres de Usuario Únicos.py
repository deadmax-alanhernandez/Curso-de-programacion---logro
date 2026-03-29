print("Creador de nombre de usuario")
prohibido = ("admin", "root", "Admin", "Root")
rechazo = []
usuario = input("Ingrese el nombre de usuario deseado: ")

while usuario in prohibido:
    print("Error, eliga otro nombre")
    rechazo.append(usuario)
    print(f"lista de rechazos: {rechazo}")
    usuario = input("Ingrese el nombre de usuario deseado: ")


print(f"Usuario creado! su nombre de usuario es {usuario}" )
#No es necesario usar ni if ni else ya que el while ya esta filtrando la respuesta#
