nro_calif=int(input("ingrese el numero alumnos: "))
cant_alumnos=0
total=0
for x in range(nro_calif):
    sum=int(input("ingrese su calificacion: "))
    
    while sum<1 or sum>5 :
        sum=0
        sum=int(input("error,ingrese su calificacion: "))

    total=sum+total


prom= total/ nro_calif
print(prom)