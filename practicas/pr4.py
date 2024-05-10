lista_original=[1,2,3,4,5,65,45,3,24,6,87]

def ordenar(lista,orden):
    if orden=="ASC":
        contador=0
        for x in range(len(lista)-1):
            for y in range(len(lista)-1):
                if lista[y]> lista[y+1]:
                    aux=lista[y]
                    lista[y]=lista[y+1]
                    lista[y+1]=aux
                
                
    
    if orden=="DESC":
        for x in range(len(lista)-1):
            for y in range(len(lista)-1):
                if lista[y] < lista[y+1]:
                    aux=lista[y]
                    lista[y]=lista[y+1]
                    lista[y+1]=aux
                
    return lista
    


print("lista original: ", lista_original)
resp=input("desea que la lista sea ascendente o descendente.ASC/DESC:  ")
if(resp=="ASC"):
    Lista_ordenada=ordenar(lista_original,"ASC")
    print("lista ordenada", Lista_ordenada)
else:
    Lista_ordenada=ordenar(lista_original,"DESC")
    print("lista ordenada", Lista_ordenada)
