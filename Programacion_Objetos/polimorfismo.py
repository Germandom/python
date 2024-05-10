class Persona:
    def __init__(self,nombre):
        self.nombre= nombre
    
    def avanza(self):
        print("ando caminando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("ando moviendome en la bicicleta")

if __name__ == "__main__":
    persona=Persona("pepe")
    persona.avanza()

    ciclista=Ciclista("jose")
    ciclista.avanza()
    