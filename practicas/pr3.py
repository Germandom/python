traductor={"agua":"water","fuego":"fire","arena":"sand", "gato":"cat"}



def ver():
    print(traductor)

while True:
    palabra=input("Ingrese una palabra: ")
    if palabra in traductor:
        print(f"{palabra} en ingles es:", traductor[palabra])
    elif palabra=="0":
        break
    else:
        print("esa palabra no se encuetra en el traductor. desea agregar al diccionario: ")
        answer=input("si/no.... ")
        if answer== "si":
            traduccion=input("ingrese la traduccion: ")
            traductor[palabra]=traduccion
            ver()
        else:
            print("palabra no fue agregada")
