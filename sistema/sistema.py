class Persona:
    nombre= None
    edad= None
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar(self):
        return f"{self.nombre}, edad: {self.edad}, "

class Empleado(Persona):
    sueldo_bruto= None
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo_bruto=sueldo

    def mostrar(self):
        return super().mostrar() + f"SN: {self.calcular_salario_neto()}"
    def calcular_salario_neto(self):
        return self.sueldo_bruto *0.9

class Cliente(Persona):
    telefono_contacto: None
    def __init__(self, nombre, edad, tel):
        super().__init__(nombre, edad)
        self.telefono_contacto=tel
    def mostrar(self):
        return super().mostrar() + f"telefono del cliente:{self.telefono_contacto}"
    
class Directivo(Empleado):
    pass
class Empresa(Cliente,Empleado):
    pass





if __name__ == "__main__":
    AA=Empleado("jose",45,6700)
    print(AA.mostrar())
    EE=Cliente("miduel",33,9997978698)
    print(EE.mostrar())

