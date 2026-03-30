print("Creador de nombre de usuario")
prohibido = ("admin", "root")
rechazo = []
usuario = input("\nIngrese el nombre de usuario deseado: ")

while usuario.lower() in prohibido:
    print("\nError, eliga otro nombre")
    rechazo.append(usuario)
    print(f"\nlista de rechazos: {rechazo}")
    usuario = input("\nIngrese el nombre de usuario deseado: ")


print(f"\nUsuario creado! su nombre de usuario es {usuario}" )
#No es necesario usar ni if ni else ya que el while ya esta filtrando la respuesta#
