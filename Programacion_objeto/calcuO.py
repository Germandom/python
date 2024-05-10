class Calculadora:
    Num1=None
    Num2=None
    resultado=None
    historial=None

    def __init__(self,n,m):
        self.Num1=n
        self.Num2=m
        self.resultado=0
        historial=[]

    def sumar(self):
        return self.Num1 +self.Num2
    def restar(self):
        return self.Num1 - self.Num2
    def multiplicar(self):
        return self.Num1 * self.Num2
    def dividir(self):
        return self.Num1 / self.Num2
    
if __name__ == "__main__":
    casio= Calculadora(40,50)
    casio2=Calculadora(30,40)
    print("suma:  ",casio.sumar())
    print("resta: ", casio.restar())
    print("multiplicacion: ", casio.multiplicar())
    print("divicion: ", casio.dividir())
    print("casio2: ", casio2.sumar())
