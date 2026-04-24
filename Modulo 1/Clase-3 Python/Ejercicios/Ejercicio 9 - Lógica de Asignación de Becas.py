print("\nlogica de asignacion de becas")

print("\nCon este programa evaluaremos si es apto como candidato al programa de becas")

promedio = float(input("\nIngrese su promedio academico con un valor del 1 al 10: "))
ingresos = int(input("\nIngrese el promedio de ingresos que genera su familia al mes: "))
conducta = (input("\n¿Posee antecedentes de ser un estudiante con buen comportamiento? (True/False): ").capitalize())
#Si uso booleano cualquier respuesta que se introduzca en conducta sera calificada como un True, la otra forma seria hacer otra variable para identificar cuando es true y cuando es false pero se me hizo mas facil de esta forma.

if promedio > 8.5 and promedio <= 10 and ingresos < 2000 and conducta == "True":
    print("\nUsted es un candidato apto para al programa de becas, prepare sus documentos para consignarlos presencialmente")

elif promedio < 0 or promedio > 10:
    print(f"\nel valor {promedio} esta fuera de los parametros")

elif conducta != "False" and conducta != "True":

    print(f"\nLa respuesta {conducta} esta fuera de los parametros") 

else:
    print("\nlo sentimos, usted no califica como candidato para la beca")