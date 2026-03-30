print("Aventura interactiva: Saliendo del refugio")

print("\nEn un mundo postapocaliptico parte de la civilizacion se tuvo que resguardar en refugios altamente equipados debido a la explosion de la guerra entre las potencias y la caida de bombas nucleares que volvieron al planeta casi inhabitable.")
print("\nCasi un siglo ha pasado y el refugio en el que te encuentras necesita una pieza crucial para reparar su sistema de depuracion de agua, debes salir al yermo para encontrar esta pieza y salvar a tu refugio.")
print("\nPero antes de eso debes atrevesar la cueva donde estaba escondido tu refugio, se te dio suministros basicos (agua y comida), ademas de un Cuchillo como herramienta.")
while True:
    ruta1 = str(input("\nCuando sales de tu refugio notas la humeda y oscura cueva que te rodea, escuchas sonidos de roedores haciendo eco con las paredes de la cueva. Hay dos caminos adonde ir, tambien puedes ingresar devuelta al refugio ¿Cual vas a tomar?: (IZQUIERDA, ADELANTE): ").upper())

    if ruta1 == "IZQUIERDA": 
        rutaiz = str(input("\nDecidiste tomar la ruta de la izquierda, esta te llevo a una zona con solo otro camino que parece estar custiodado por un grupo de ratas, en la zona tambien hay un cadaver de otro morador de refugio y al lado de este hay lo que parece un explosivo improvisado que perfectamente puedes recoger, tambien tienes un cuchillo de supervivencia que se te dio previamente, podrias usarlo para atacarlos pero estas ratas parecen mas fuertes de lo normal, tambien piensas en tirar un poco de tu comida para distraer a las ratas, en que quedarias con menos suministros. ¿Que haces? (RECOGER, ATACAR, TIRAR )").upper())
        if rutaiz == "RECOGER":
            bomba = str(input("\nDecides recoger la bomba que se encontraba junto al cadaver ¿Que decides hacer?: (GUARDARLA, TIRARLA, CONSUMIRLA)").upper())
            if bomba == "TIRARLA":
                print("\nLanzas la bomba contra el grupo de ratas, la explosion retumba la cueva. Matas a las ratas, pero todo empieza a temblar y luego a derrumbarse. Escombros caen y sellan el camino de donde saliste y la otra salida de la zona. Finalmente quedaste atrapado, no fue muy buena idea tirar una bomba en un lugar cerrado.")
                print("\nGAME OVER")
            elif bomba == "CONSUMIRLA":
                print("\n¿Pero que haces? ¿Porque se te ocurre consumir una bomba ENTERA?. Al ser una bomba creada con materiales muy volatiles al ingresar a tu cuerpo explota, causando que termines en mil pedazos")
                print("\nGAME OVER")
            elif bomba == "GUARDARLA":
                guardar = str(input("\nDecides almacenar la bomba por si la necesitas, en otra ocasion. Parece que las ratas se dispersaron un poco como para escubillirte o para salir corriendo directamente a la salida. ¿Que haces ahora?: (CORRER, ESCABULLIRSE, QUEDARSE)").upper())
                if guardar == "QUEDARSE":
                    print("\nTe quedas quieto en tu sitio, las ratas notan tu presencia y se abalanzan sobre ti")
                    print("\nGAME OVER")
                elif guardar == "CORRER":
                    print("\nEmpiezas a correr y el ruido atrae a las ratas")
                    print("\nEmpieza una persecucion pero empiezas a ver una luz al final del tunel")
                    print("\nAl casi llegar a esta luz notas algo")
                    print("\nHay una criatura gigante parecida a una rata en la entrada que te tapa el camino")
                    print("\nEntre la horda de ratas y esta criatura terminas acorralado")
                    huida = input("\nQue haces ahora? (ESQUIVAR, MORIR, LUCHAR)").upper()
                    if huida == "ESQUIVAR":
                        print("\nBuscas donde escabullirte, y intentas pasar a un lado de la criatura mientras te siguen las ratas")
                        print("\nPero al intentar cruzar su lateral sientes un zarpaso, la criatura te ataco")
                        print("\nSus garras son los suficientemente fuertes como para tumbarte, estas acabado")
                        print("\nGAME OVER")
                    elif huida == "MORIR":
                        print("\nSimplemente aceptas tu destino, que mas da no?")
                        print("\nGAME OVER")
                    elif huida == "LUCHAR":
                        print("\nNo te rindes y decides usar todo lo que tienes")
                        print("\nBuscas en tu mochila y ves tu comida y la granada")
                        print("\nSacas el cuchillo y abres la comida esparciendola lejos de ti")
                        print("\nLas ratas pequeñas se alejan a buscar esta comida")
                        print("\nAhora solo queda la gigante")
                        ultima = print("Que haces ahora? (CUCHILLO/BOMBA/COMIDA)").upper()
                        if ultima == "CUCHILLO":
                            print("\nUsas tu cuchillo para luchar con la criatura")
                            print("\nSe lo buscas clavar en sus puntos blandos, como los ojos")
                            print("\nAmbos luchan por su vida")
                            print("\nLa fuerza de la criatura te supera y de un zarpaso, la pelea acaba")
                            print("\nGAME OVER")
                        elif ultima == "BOMBA":
                            print("\nDecides usar la bomba que recogiste antes") 
                            print("\nLe quitas el seguro para preparar tu movimiento")
                            print("\nLa criatura ataca pero lo esquivas de a poco")
                            print("\nSe acaba el tiempo, decides hacer tu movimiento YA")
                            print("\nTerminas poniendo la bomba en la boca de la criatura y sales corriendo hacia la salida")
                            print("\nla bomba termina estallando y la criatura vuela en mil pedazos")
                            print("\nLogras salir del lugar victorioso, y al fin llegaste a la salida")
                            print("\nPor primera vez en tu vida llegas al exterior, con una luz constante estremecedora en el cielo")
                            print("\nEste solo es el comienzo, tendras que hacer mucho mas de ahora en adelante...") 
                            print("\nFINAL 1")   
                            break
                        elif ultima == "COMIDA":
                            print("\nArrojas el poco de comida que quedo en el recipiente")
                            print("\nLa rata gigante la mira con curiosidad un segundo")
                            print("\nLuego concluye que va a preferir algo mas grande")
                            print("\nLo siguiente que sabes es que todo se ve oscuro")
                            print("\nGAME OVER")
                        else:
                            print("\nOpcion no valida")
                    else:
                        print("\nOpcion no valida")
                elif guardar == "ESCABULLIRSE":
                    print("\nVas sigilosamente hacia el camino para evitar que las ratas te vean y pasas")
                    print("\nEmpiezas ver una luz que aperenta ser el exterior")
                    print("\nPero cuando te estas acercando notas algo")
                    print("\nHay una enorme criatura durmiendo en el medio del pasillo, un movimiento en falso y estas muerto")
                    final = input("\nComo avanzas? (IZQ, DERECHA)").upper()
                    if final == "IZQ":
                        print("\nTe escabulles por la izquierda")
                        print("\nLo estas logrando, pero sin querer chocas con algo")
                        print("\nEs la cola de la criatura, termina despertando con colera")
                        print("\nSe abalanza sobre ti y empieza a morderte con sus enormes dientes de rata")
                        print("\nIntentas luchas pero del dolor terminas cediendo")
                        print("\nGAME OVER")       
                    elif final == "DERECHA":
                        print("\nVas por la derecha, notas unas piedras pero las evitas")
                        print("\nYa pasaste a la criatura quien sigue durmiendo placidamente")
                        print("\nVes la salida, no lo puedes creer")
                        print("\nLograste llegar por fin")
                        print("\nMiras a tu alrededor, es la primera vez que estas afuera del refugio")
                        print("\nAqui comienza tu aventura")
                        print("\nFINAL 2")   
                    else:
                        print("\nOpcion no valida")
            else:
                print("\nOpcion no valida")   
        elif rutaiz == "ATACAR":
            print("\nVas contra la horda de ratas con tu cuchillo")
            print("\nEmpiezas a llevarte a unas cuantas, tienes posibilidades de ganar")
            print("\nTe empiezas a cansar y todavia quedan muchas")
            print("\nTe superan en numero, no das abasto")
            print("\nDan su contraataque y se abalanzan contra ti")
            print("\nNo puedes mas, subestimaste a tu enemigo")
            print("\nGAME OVER")
        elif rutaiz == "TIRAR":
            print("\nDecides tirar tu comida para ver si las ratas se distraen")
            print("\nUn grupo de ratas se queda velando por la comida")
            print("\nPero otro gracias a la direccion de la que lo tiraste notan tu presencia")
            print("\nParece que quieren un aperitivo mas grande")
            print("\nGAME OVER")
        else: 
            print("\nOpcion no valida")
    elif ruta1 == "ADELANTE":
        print("\nSigues hacia adelante pero te encuentras un camino sin salida")
    else: 
        print("\nOpcion no valida")
