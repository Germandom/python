notas=[]
suma=0
for x in range(1,4):
    nota=int(input(f"Ingrese la nota {x}:"))
    while(nota<1 or nota>5):
        nota=int(input("ERROR:Ingrese la nota de nuevo: "))
    notas.append(nota)
    suma=suma+nota

promedio=suma/3
print("Su promedio es: %.1f"%(promedio))
print("estado: ")
if (promedio> 1.7):
    print("aprobado")
else:
    print("Reprobado")