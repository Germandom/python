num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))

if(num1>num2):
    print("{} es mayor a {}".format(num1,num2))
    if(num1 % 2 == 0):
        print("es par")
    else:
        print("es impar")
elif(num1<num2):
    print("{} es mayor que {}".format(num2, num1))
    if(num2 % 2 == 0):
        print("es par")
    else:
        print("es impar")
else:
    print("Los numeros son iguales")

print("--------------------------------------------")
usuario=input("Ingrese su usuario:")
password= input("Ingrese su contreseña:")

if (usuario== "admin" and password== "123456"):
    print("acceso correcto")
else:
    print("acceso incorrecto")