dic={"admin1":"12345", "admin2":"99999", "admin3":"easymoneysniper"}

intentos=1
usuario=input("ingrese su usuario: ")

while(intentos<4):
    if usuario in dic:
        print("usuario correcto")
        password= input("Ingrese su contreseña: ")
        if(password == dic[usuario]):
            print("contraseña correcta")
            print("..........")
            intentos=5
        else:
            print("contraseña incorrecta")
            intentos +=1
    else :
       print("error.no encotrado")
       intentos += 1



