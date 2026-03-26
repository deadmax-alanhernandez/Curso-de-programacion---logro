print("\nconversion de calificaciones")

nota = float(input("\nInserte su calificacion del examen: "))

if nota >= 90 and nota <= 100:
    print("\nFelicidades, has obtenido una A!!")

elif nota >= 80 and nota <= 89:
    print("\nBastante bien, has obtenido una B!")

elif nota >= 70 and nota <= 79:
    print("\nLo intestaste que es lo importante. Has obtenido una C")

elif nota >= 60 and nota <= 69:
    print("\nPor poco y aprobaste. Has obtenido una D")

elif nota >= 0 and nota <= 59:
    print("\nEstudia mas para la proxima, desaprobaste. Has obtenido una F")

else:
    print("\nError, parametro no valido")






