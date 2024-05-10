#funciones matematicas

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a+ b
def divisio(a,b):
    if(b==0):
        return "no se puede dividir por cero"
    else:
        return a/b
def raiz(a,b=2):
    return a**1/b

if __name__ == '__main__' :
    print ("la suma de 3 y 4 son  ",suma(3,4))
