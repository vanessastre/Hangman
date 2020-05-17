def dibujarAhorcado(intentos,palabra):
    if (intentos==0):
        print("___________\n|         |\n|\n|\n|\n|\n|__________")
    elif (intentos==1):
        print("___________\n|         |\n|         O\n|\n|\n|\n|__________")
    elif (intentos==2):
        print("___________\n|         |\n|         O\n|         |\n|         |\n|\n|__________")
    elif (intentos==3):
        print("___________\n|         |\n|         O\n|        \|\n|         |\n|\n|__________")
    elif (intentos==4):
        print("___________\n|         |\n|         O\n|        \|/\n|         |\n|\n|__________")
    elif (intentos==5):
        print("___________\n|         |\n|         O\n|        \|/\n|         |\n|        /\n|__________")
    elif (intentos==6):
        print("___________\n|         |\n|         O\n|        \|/\n|         |\n|        / \ \n|__________")
        print("\n Perdiste! \n")
        print("\n La pelicula era: ",palabra)
        jugarNuevamente()
        return
def esconderLaPalabra(listaPalabras,listaEspacios):
    for letter in listaPalabras:
        if letter!=" ":
            listaEspacios.append("_")
        else:
            listaEspacios.append(" ")
    return

def gano():
    print("\n Ganaste!!!")
    jugarNuevamente()
    quit()

def jugarNuevamente():
    jugardenuevo=input("\n Quieres jugar de nuevo? Si/No \n").upper()
    if (jugardenuevo=="SI"):
        ahorcado()
    else:
        print("Gracias por jugar conmigo al ahorcado")
    return

def ahorcado():
    intentos=0
    palabra= input("\n Escribe la pelicula a adivinar \n").upper()
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
    listaPalabras= list(palabra)
    listaEspacios=[]
    esconderLaPalabra(listaPalabras,listaEspacios)
    nuevaListaEspacios= listaEspacios.copy()
    listaIntentos= []
    print("Bienvenido al ahorcado.\nTienes que adivinar la pelicula\n")
    dibujarAhorcado(intentos,palabra)
    print (" ".join(listaEspacios))
    while intentos<6:
        arriesga= input("\n Quieres arriesgar?  Si/No ").upper()
        if arriesga=="SI":
            arriesgo=input("\n Escribe el titulo de la pelicula: ").upper()
            if arriesgo==palabra:
                gano()
            else:
                print("Esa no es la pelicula")
        letra=input("\n Escribe una letra:  ").upper()
        if len(letra)>1:
            print("\n Solo una letra!!!\n")
        elif letra=="":
            print("\n Tienes que escribir una letra\n")
        elif letra in listaIntentos:
            print("\n Esa letra ya la dijiste \n")
            print("Estas son las letras que ya dijiste: ",listaIntentos)
            print("\n")
        else:
            listaIntentos.append(letra)
            i=0
            while i< len(palabra):
                if letra==listaPalabras[i]:
                    nuevaListaEspacios[i]=letra
                i= i+1
            if nuevaListaEspacios==listaEspacios:
                print("\n Esa letra no esta \n")
                intentos= intentos + 1
                dibujarAhorcado(intentos,palabra)
                if intentos<6:
                    print("\n Intenta de nuevo \n")
                    print(" ".join(listaEspacios))
            elif listaPalabras != listaEspacios:
                listaEspacios= nuevaListaEspacios[:]
                dibujarAhorcado(intentos,palabra)
                print(" ".join(listaEspacios))
                if listaPalabras == listaEspacios:
                    gano()
                else:
                    print ("\n Bieeeeeeeeeeeen! Ahora otra \n")
ahorcado()