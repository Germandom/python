from biblioteca import Biblioteca
from libro import Libro

if __name__ == "__main__":
    ejecutar=True
    while ejecutar:
        print("...BIENVENIDO AL SISTEMA BIBLIOTECARIO...")
        opcion=int(
            input(
                "Que vas a hacer hoy?: \n1-Crear Biblioteca\n2-Agregar Libro\n3-Ver Catalogo\n4-Quitar libro\n5-Salir\n... :"
            )
        )
        if opcion ==1 :
            nombre =input("Nombre de la biblioteca: ")
            biblioteca=Biblioteca(nombre)
            print("se creo la biblioteca {}".format(biblioteca.consultar_nombre_biblioteca()))
        elif opcion==2:
            titulo=input("Titulo: ")
            autor=input("Autor: ")
            cantidad_de_paginas=input("Paginas: ")
            genero=input("Genero: ")
            sinopsis=input("Sinopsis: ")

            libro=Libro(titulo,autor,cantidad_de_paginas,genero,sinopsis)
            biblioteca.agregar_libro(libro)
        elif opcion==3:
            print("Catalogo de Libros: ")
            for i in biblioteca.consultar_libros():
                print(i)
        elif opcion==4:
            indice=input("ID del libro a quitar: ")
            biblioteca.quitar_libro(indice)
        elif opcion==5:
            print("Gracias por visitar. \n")
            ejecutar=False
        else:
            print("opcion incorrecta...")