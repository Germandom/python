import os

resp=1
while resp !=0:
    print("Paint(1)")
    print("calc(2)")
    print("Apagar pc en 2 horas(3)")
    print("salir(0)")
    resp=int(input("seleccione: "))
    if resp ==1:
        os.system("mspaint")
    elif(resp ==2):
        os.system("calc")
    elif( resp == 3):
        os.system("shutdowm -s -t 7200")
    else:
        print("No entiendo esa orden...")