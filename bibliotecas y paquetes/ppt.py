import random
while True:
    aleatorio = random.randrange(0,3)
    eligePc = ""
    print("1.Piedra")
    print("2.Papel")
    print("3.Tijera")
    opccion=int(input("Elige tu opcion:"))

    if opccion==1:
        eligeUser="Piedra"
    elif opccion==2:
        eligeUser="Papel"
    elif opccion==3:
        eligeUser="Tijera"
    print("Elegiste: ", eligeUser)

    if aleatorio==0:
        eligePc="Piedra"
    elif aleatorio==1:
        eligePc="Papel"
    elif aleatorio==2:
        eligePc="Tijeras"
    print("la maquina eligio: ", eligePc)
    print("..............")

    if eligePc=="Piedra" and eligeUser=="Papel":
        print("Ganaste.Papel envuelve piedra")
        print(".............")
    elif eligePc=="Papel" and eligeUser=="Tijera":
        print("Ganaste.Tijera corta Papel")
        print(".............")
    elif eligePc=="Tijeras" and eligeUser=="Piedra":
        print("Ganaste.Piedra aplazta Tijera")
        print(".............")
    if eligePc=="Papel" and eligeUser=="Piedra":
        print("Perdite.Papel envuelve piedra")
        print(".............")
    elif eligePc=="Tijeras" and eligeUser=="Papel":
        print("Perdiste.Tijera corta Papel")
        print(".............")
    elif eligePc=="Piedra" and eligeUser=="Tijera":
        print("Perdiste.Piedra aplazta Tijera")
        print(".............")
    elif eligeUser==eligePc:
        print("empate")
        print(".............")