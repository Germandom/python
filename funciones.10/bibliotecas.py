import os

#menu principal
respuesta=-1
while (respuesta !=0):
    print("eliga una opcion")
    print("1.Calculadora")
    print("2.ver mi ip")
    print("3.administrador de tareas")
    print("4.Apagar equipo en 5 min")
    print("5.Cancelar apagado")
    print("0.salir")
    respuesta = int(input(""))
    if(respuesta==1):
        os.system('calc')
    elif(respuesta==2):
        os.system('ipconfig')
    elif(respuesta==3):
        os.system('taskmgr')
    elif(respuesta==4):
        os.system('shutdowm -s -t -300')
    elif(respuesta==5):
        os.system('shutdowm /a')
    else:
        "no se ha seleccionado nada"
    