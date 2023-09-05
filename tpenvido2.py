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





pre_envidoJ1=0
pre_envidoJ2=0


def envido(array_carta, array_envido):
    if array_carta[0][1]== array_carta[1][1]:      #SI EL PALO DE LA PRIMERA CARTA ES IGUAL AL PALO DE LA SEGUNDA
        array_envido=20
        if array_carta[0][0] not in (10, 11, 12) and array_carta[1][0] not in (10, 11, 12):     #SI LOS NUMEROS DE LAS 2 CARTAS NO SON 10-11-12, SE SUMAN
            array_envido+=array_carta[0][0] +array_carta[1][0]
        elif array_carta[0][0] in (10, 11, 12) and array_carta[1][0] in (10, 11, 12):           #SI LOS NUMEROS DE LAS 2 CARTAS SON 10-11-12, NO SUMA NADA
            array_envido+=0
        elif array_carta[0][0] not in (10, 11, 12) and array_carta[1][0]in (10, 11, 12):       #SI LOS NUMEROS DE LA PRIMERA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA PRIMERA
            array_envido+=array_carta[0][0]
        elif array_carta[0][0]in (10, 11, 12) and array_carta[1][0] not in (10, 11, 12):       #SI LOS NUMEROS DE LA SEGUNDA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA SEGUNDA
            array_envido+=array_carta[1][0]


    elif array_carta[0][1] == array_carta[2][1]:    #SI EL PALO DE LA PRIMERA CARTA ES IGUAL AL PALO DE LA TERCERA
        array_envido=20
        if array_carta[0][0] not in (10, 11, 12) and array_carta[2][0] not in (10, 11, 12):     #SI LOS NUMEROS DE LAS 2 CARTAS NO SON 10-11-12, SE SUMAN
            array_envido+=array_carta[0][0] + array_carta[2][0]

        elif array_carta[0][0] in (10, 11, 12) and array_carta[2][0] in (10, 11, 12):           #SI LOS NUMEROS DE LAS 2 CARTAS SON 10-11-12, NO SUMA NADA
            array_envido+=0

        elif array_carta[0][0] not in (10, 11, 12) and array_carta[2][0] in (10, 11, 12):       #SI LOS NUMEROS DE LA PRIMERA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA PRIMERA
            array_envido+=array_carta[0][0]

        elif array_carta[0][0] in (10, 11, 12) and array_carta[2][0] not in (10, 11, 12):       #SI LOS NUMEROS DE LA SEGUNDA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA SEGUNDA
            array_envido+=array_carta[2][0]
        

    elif array_carta[2][1] == array_carta[1][1]:    #SI EL PALO DE LA TERCERA ES IGUAL AL PALO DE LA SEGUNDA
        array_envido=20
        if array_carta[2][0] not in (10, 11, 12) and array_carta[1][0] not in (10, 11, 12):     #SI LOS NUMEROS DE LAS 2 CARTAS NO SON 10-11-12, SE SUMAN
            array_envido+=array_carta[2][0] + array_carta[1][0]

        elif array_carta[2][0] in (10, 11, 12) and array_carta[1][0] in (10, 11, 12):           #SI LOS NUMEROS DE LAS 2 CARTAS SON 10-11-12, NO SUMA NADA
            array_envido+=0

        elif array_carta[2][0] not in (10, 11, 12) and array_carta[1][0] in (10, 11, 12):       #SI LOS NUMEROS DE LA PRIMERA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA PRIMERA
            array_envido+=array_carta[2][0]

        elif array_carta[2][0] in (10, 11, 12) and array_carta[1][0] not in (10, 11, 12):       #SI LOS NUMEROS DE LA SEGUNDA CARTA NO SON 10-11-12, PERO DE LA SEGUNDA SI, SE SUMA SOLO LA SEGUNDA
            array_envido+=array_carta[1][0]


    elif array_carta[2][1] == array_carta[1][1] == array_carta[0][1]:     #SITUACION FLOR
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
    
    elif array_carta[2][1] != array_carta[1][1] != array_carta[0][1]:     #SITUACION TODOS DISTINTOS
        templist=[]
        templist.extend([array_carta[2][0], array_carta[1][0], array_carta[0][0]])
        templist.sort(reverse=True)
        if templist[0] not in (10,11,12):
            array_envido+=templist[0]
        elif templist[1] not in (10, 11, 12):
            array_envido+=templist[1]
        elif templist[2] not in (10, 11,12):
            array_envido+=templist[2]
        else:
            array_envido=0

        

    array_envido = int(array_envido)
    return array_envido


carta(cartasJ1)
carta(cartasJ2)
print(cartasJ1)
print(cartasJ2)
print(cartasJ1[0][1])
print(cartasJ1[1][1])

print(f'Carta 1 de usuario: {cartasJ1[0][0]} de {cartasJ1[0][1]}')



envidoJ1= envido(cartasJ1,pre_envidoJ1)
envidoJ2 = envido(cartasJ2,pre_envidoJ2)
print("Valor del envido J1:", envidoJ1)
print("Valor del envido J2:", envidoJ2)









