
#IF
llueve= True
feriado= False

if llueve == True or feriado == True:
    print("me quedo en casa")
else:
    print("me voy")

#IF ELSE

mal=True

if mal == True:
    print("no salgo de casa")
else:
    print("salgo de casa")

    #IF ELIF ELSE

x = int(input("ingrese un numero: "))

if x>100:
    print("es mayor que 100")
elif x==100:
    print("es igual a 100")
else :
    print("es menor que 100")