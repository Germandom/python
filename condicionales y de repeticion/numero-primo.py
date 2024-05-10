num=100000000
while True:
    bandera=0
    for x in range(2,num//2):
        if(num % x == 0):
            bandera=1
            break #para romper el primer bucle
    if(bandera==0):
        print(num)
    bandera=0
    num +=1
