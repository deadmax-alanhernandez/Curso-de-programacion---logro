print("Aventura interactiva: Saliendo del refugio")

print("\nEn un mundo postapocaliptico parte de la civilizacion se tuvo que resguardar en refugios altamente equipados debido a la explosion de la guerra entre las potencias y la caida de bombas nucleares que volvieron al planeta casi inhabitable. Casi un siglo ha pasado y el refugio en el que te encuentras necesita una pieza crucial para reparar su sistema de depuracion de agua, debes salir al yermo para encontrar esta pieza y salvar a tu refugio. Pero antes de eso debes atrevesar la cueva donde estaba escondido tu refugio, se te dio suministros basicos (agua y comida), ademas de un Cuchillo y una bengala como herramientas.")

ruta1 = str(input("Cuando sales de tu refugio notas la humeda y oscura cueva que te rodea, escuchas sonidos de roedores haciendo eco con las paredes de la cueva. Hay dos caminos adonde ir, tambien puedes ingresar devuelta al refugio ¿Cual vas a tomar?: (IZQUIERDA, ADELANTE, ATRAS ): ").upper())

if ruta1 == "IZQUIERDA":
    rutaiz = str(input("Decidiste tomar la ruta de la izquierda, esta te llevo a una zona con solo otro camino que parece estar custiodado por un grupo de ratas, en la zona tambien hay un cadaver de otro morador de refugio y al lado de este hay lo que parece un explosivo improvisado que perfectamente puedes recoger, tambien tienes un cuchillo de supervivencia que se te dio previamente, podrias usarlo para atacarlos pero estas ratas parecen mas fuertes de lo normal, tambien piensas en tirar un poco de tu comida para distraer a las ratas, en que quedarias con menos suministros. ¿Que haces? (RECOGER, ATACAR, TIRAR )").upper())
    if rutaiz == "RECOGER":
        bomba = str(input("Decides recoger la bomba que se encontraba junto al cadaver ¿Que decides hacer?: (GUARDARLA, TIRARLA, CONSUMIRLA)").upper())
        if bomba == "TIRARLA":
            print("Lanzas la bomba contra el grupo de ratas, la explosion retumba la cueva. Matas a las ratas, pero todo empieza a temblar y luego a derrumbarse. Escombros caen y sellan el camino de donde saliste y la otra salida de la zona. Finalmente quedaste atrapado, no fue muy buena idea tirar una bomba en un lugar cerrado.")
            print("GAME OVER")
        elif bomba == "CONSUMIRLA":
            print("¿Pero que haces? ¿Porque se te ocurre consumir una bomba ENTERA?. Al ser una bomba creada con materiales muy volatiles al ingresar a tu cuerpo explota, causando que termines en mil pedazos")
            print("GAME OVER")
        elif bomba == "GUARDARLA":
            guardar = str(input("Decides almacenar la bomba por si la necesitas, en otra ocasion. Parece que las ratas se dispersaron un poco como para escubillirte o para salir corriendo directamente a la salida. ¿Que haces ahora?: (CORRER, ESCARBULLISE, QUEDARSE)").upper())
            if guardar == "QUEDARSE":

