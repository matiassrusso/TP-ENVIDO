import random

cartasJ1=[[],[],[]]

cartasJ2=[[],[],[]]

def num_carta():                        #CREADOR NUMERO DE CARTA RANDOM
    cartas = [c for c in range(1, 12) if c not in [8, 9]]
    numcarta=random.choice(cartas)
    #print(numcarta)
    return numcarta

def palo_carta():                       #CREADOR PALO RANDOM
    palos=['Oro','Basto','Espada','Copa']
    palocarta=random.choice(palos)
    #print(palocarta)
    return palocarta


def carta(array_carta):                  #CREADOR CARTAS [numero, palo]
    array_carta[0].clear()
    array_carta[1].clear()
    array_carta[2].clear()

    array_carta[0].extend([num_carta(), palo_carta()])
    array_carta[1].extend([num_carta(), palo_carta()])
    array_carta[2].extend([num_carta(), palo_carta()])

carta(cartasJ1)
carta(cartasJ2)


totenvido=[0,0]
envidoJ1=totenvido[0]
envidoJ2=totenvido[1]


def envido(array_carta, array_envido):
    if array_carta[0][1] in array_carta[0] == array_carta[1][1] in array_carta[1]:      #SI EL PALO DE LA PRIMERA CARTA ES IGUAL AL PALO DE LA SEGUNDA
        array_envido=20
        if array_carta[0][0] in array_carta[0] not in (10, 11, 12) and array_carta[1][0] in array_carta[1] not in (10, 11, 12):     #SI LOS NUMEROS DE LAS 2 CARTAS NO SON 10-11-12, SE SUMAN
            array_envido+=array_carta[0][0] in array_carta[0]+array_carta[1][0]in array_carta[1]
        elif array_carta[0][0] in array_carta[0] in (10, 11, 12) and array_carta[1][0] in array_carta[1] in (10, 11, 12):           #SI LOS NUMEROS DE LAS 2 CARTAS SON 10-11-12, NO SUMA NADA
            array_envido+=0
        elif array_carta[0][0] in array_carta[0] not in (10, 11, 12) and array_carta[1][0] in array_carta[1] in (10, 11, 12):       #SI LOS NUMEROS DE LA PRIMERA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA PRIMERA
            array_envido+=array_carta[0][0]
        elif array_carta[0][0] in array_carta[0] in (10, 11, 12) and array_carta[1][0] in array_carta[1] not in (10, 11, 12):       #SI LOS NUMEROS DE LA SEGUNDA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA SEGUNDA
            array_envido+=array_carta[1][0]


    elif array_carta[0][1] in array_carta[0] == array_carta[2][1] in array_carta[2]:    #SI EL PALO DE LA PRIMERA CARTA ES IGUAL AL PALO DE LA TERCERA
        array_envido=20
        if array_carta[0][0] in array_carta[0] not in (10, 11, 12) and array_carta[2][0] in array_carta[2] not in (10, 11, 12):     #SI LOS NUMEROS DE LAS 2 CARTAS NO SON 10-11-12, SE SUMAN
            array_envido+=array_carta[0][0] in array_carta[0]+array_carta[2][0]in array_carta[2]

        elif array_carta[0][0] in array_carta[0] in (10, 11, 12) and array_carta[2][0] in array_carta[2] in (10, 11, 12):           #SI LOS NUMEROS DE LAS 2 CARTAS SON 10-11-12, NO SUMA NADA
            array_envido+=0

        elif array_carta[0][0] in array_carta[0] not in (10, 11, 12) and array_carta[2][0] in array_carta[2] in (10, 11, 12):       #SI LOS NUMEROS DE LA PRIMERA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA PRIMERA
            array_envido+=array_carta[0][0]

        elif array_carta[0][0] in array_carta[0] in (10, 11, 12) and array_carta[2][0] in array_carta[2] not in (10, 11, 12):       #SI LOS NUMEROS DE LA SEGUNDA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA SEGUNDA
            array_envido+=array_carta[2][0]
        

    elif array_carta[2][1] in array_carta[2] == array_carta[1][1] in array_carta[1]:    #SI EL PALO DE LA TERCERA ES IGUAL AL PALO DE LA SEGUNDA
        array_envido=20
        if array_carta[2][0] in array_carta[2] not in (10, 11, 12) and array_carta[1][0] in array_carta[1] not in (10, 11, 12):     #SI LOS NUMEROS DE LAS 2 CARTAS NO SON 10-11-12, SE SUMAN
            array_envido+=array_carta[2][0] in array_carta[2]+array_carta[1][0]in array_carta[1]

        elif array_carta[2][0] in array_carta[2] in (10, 11, 12) and array_carta[1][0] in array_carta[1] in (10, 11, 12):           #SI LOS NUMEROS DE LAS 2 CARTAS SON 10-11-12, NO SUMA NADA
            array_envido+=0

        elif array_carta[2][0] in array_carta[2] not in (10, 11, 12) and array_carta[1][0] in array_carta[1] in (10, 11, 12):       #SI LOS NUMEROS DE LA PRIMERA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA PRIMERA
            array_envido+=array_carta[2][0]

        elif array_carta[2][0] in array_carta[2] in (10, 11, 12) and array_carta[1][0] in array_carta[1] not in (10, 11, 12):       #SI LOS NUMEROS DE LA SEGUNDA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA SEGUNDA
            array_envido+=array_carta[1][0]


    elif array_carta[2][1] in array_carta[2] == array_carta[1][1] in array_carta[1] == array_carta[0][1] in array_carta[0]:     #SITUACION FLOR
        array_envido=20
        if array_carta[2][0] not in (10,11,12) and array_carta[1][0] not in (10,11,12) and array_carta[0][0] not in (10,11,12):
            templist=[]
            templist.extend([array_carta[2][0], array_carta[1][0], array_carta[0][0]])
            templist.sort(reverse=True)
            array_envido+=templist[0]+templist[1]

        elif array_carta[2][0] in (10,11,12) and array_carta[1][0] not in (10,11,12) and array_carta[0][0] not in (10,11,12):
            array_envido+=array_carta[1][0]+array_carta[0][0]

        elif array_carta[2][0] not in (10,11,12) and array_carta[1][0] in (10,11,12) and array_carta[0][0] not in (10,11,12):
            array_envido+=array_carta[2][0]+array_carta[0][0]

        elif array_carta[2][0] not in (10,11,12) and array_carta[1][0] not in (10,11,12) and array_carta[0][0] in (10,11,12):
            array_envido+=array_carta[1][0]+array_carta[2][0]



num_carta()
palo_carta()
print(cartasJ1)
print(cartasJ2)
print(cartasJ1[0][1])
print(f'Carta usuario: {cartasJ1[0][0]} de {cartasJ1[0][1]}')
templist=[]
x=0
templist.extend([cartasJ1[2][0], cartasJ1[1][0], cartasJ1[0][0]])
templist.sort(reverse=True)
print(templist)
x=templist[0]+templist[1]
print(x)







