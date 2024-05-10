agenda={}

def cargar_agenda(nom, num):
    agenda[nom]=num

def ver_agenda():
    print(agenda)

def ver_agenda_detalle():
    print("Lista de contactos: ")
    for nom,num in agenda.items():
        print(f"{nom} : {num}")

if __name__ =="__main__":
    cargar_agenda("Josepo", "0992324234")
    cargar_agenda("Mariana", "0971123456")
    ver_agenda()
    ver_agenda_detalle()

