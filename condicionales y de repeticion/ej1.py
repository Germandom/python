x=int(input("ingrese un numero: "))
y=int(input("ingrese un numero: "))

if x>y:
    print("{} es mayor".format(x))
    if (x % 2 == 0):
        print("es par")
    else:
        print("es impar")
elif y>x:
    print("{} es mayor ".format(y))
    if(y % 2 ==0):
        print("es par")
    else:
        print("es impar")
else:
    print("son iguales ")