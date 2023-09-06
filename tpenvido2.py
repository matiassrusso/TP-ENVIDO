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

#SISTEMA DE TURNOS
#SI SALE 1, ES EL TURNO DEL J1. SI SALE 2, ES EL TURNO DEL J2.
#PARA QUE LA MAQUNA DECIDA, SE VA A SORTEAR UN NUMERO ENTRE EL 1 Y EL 1000.
#SI LA MAQUINA ES MANO, PASA ESTO:                  #osea si el tuno sale 2          
#    SI EL NUMERO ESTA ENTRE 1 Y 750, LA MAQUINA VA A QUERER JUGAR ENVIDO NORMAL
#    SI EL NUMERO ESTA ENTRE EL 751 Y 1000, VA A PASAR.

#SI LA MAQUINA NO ES MANO, PASA ESTO:               #osea si el turno sale 1
#       SI EL NUMERO ESTA ENTRE 1 Y 600, LA MAQUINA VA A QUERER JUGAR ENVIDO NORMAL.
#       SI EL NUMERO ESTA ENTRE EL 601 Y 900, LA MAQUINA NO VA A QUERER JUGAR ENVIDO.
#       SI EL NUMERO ESTA ENTRE EL 901 Y EL 1000, SI NO ES MANO, VA A QUERER ENVIDO ENVIDO
    
#SI YO SOY MANO, Y PASO, TURNO PASA A SER 2.
#SI YO LE CANTO ENVIDO ENVIDO, LAS CHANCES SON 50/50




def numero_random(intmaq):
    intmaq.clear()
    intmaq=random.randint(1, 1000)
    return intmaq
    
#Juego
turno_maq=0
puntosJ1=0
puntosJ2=0
while puntosJ1<0 and puntosJ2<0:
    carta(cartasJ1)
    carta(cartasJ2)
    turno=random.randint(1, 2)
    numero_random(turno_maq)
    envidoJ1= envido(cartasJ1,pre_envidoJ1)
    envidoJ2 = envido(cartasJ2,pre_envidoJ2)
   
    if turno==1:
        J1=input(f'Es tu turno. Tus castas son: {cartasJ1[0][0]} de {cartasJ1[0][1]}, {cartasJ1[1][0]} de {cartasJ1[1][1]}, y {cartasJ1[2][0]} de {cartasJ1[2][1]}. Tenes un envido de {envidoJ1}. Canta envido o pasa. ')
        J1= J1.lower()
        if J1 == 'envido':
            if turno_maq<= 600:
                print('Maquina: Quiero.')
                if envidoJ1>envidoJ2:
                    puntosJ1+=3
                    print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                elif envidoJ2>envidoJ1:
                    puntosJ2+=3
                    print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                elif envidoJ1==envidoJ2:
                    puntosJ1+=3
                    print(f'Tenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
            
            elif 600<turno_maq<=900:
                print('Maquina: No quiero.')
                puntosJ1+=3
                print(f'Ganaste. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                
            elif 901<turno_maq<=1000:
                J1=input('Maquina: Envido envido. ')
                J1= J1.lower()
                if J1 == 'quiero':
                    if envidoJ1>envidoJ2:
                        puntosJ1+=4
                        print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=4
                        print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ1+=4
                        print(f'Tenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                elif J1 == 'no quiero':
                    puntosJ2+=3
                    print(f'Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
        
        elif J1 == 'paso':
            #numero_random(turno_maq)
            #turno = 2
            if turno_maq<=750:
                print('Maquina: Bueno ahora es mi turno. Envido')
                J1=input(f'Tenes un envido de {envidoJ1}. Queres envido, no queres, o queres envido envido? ')
                J1 = J1.lower()
                if J1 == 'quiero':
                    if envidoJ1>envidoJ2:
                        puntosJ1+=3
                        print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=3
                        print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ1+=2
                        print(f'Tenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                elif J1 == 'no quiero':
                    puntosJ2+=3
                    print(f'No quisiste. Se le suman 3 a la maquina. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')

                elif J1 == 'envido envido':
                    numero_random(turno_maq)
                    if turno_maq <= 500:
                        print('Maquina: Quiero')
                        if envidoJ1>envidoJ2:
                            puntosJ1+=4
                            print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                        elif envidoJ2>envidoJ1:
                            puntosJ2+=4
                            print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                        elif envidoJ1==envidoJ2:
                            puntosJ2+=4
                            print(f'Tenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                    elif 500<turno_maq<=1000:
                        print('Maquina: No quiero.')
                        puntosJ1+=4
                        print(f'Ganaste. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
            elif 750<turno_maq<=1000:
                print('Maquina: Paso.')
                print(f'La maquina paso. No se le suman puntos a nadie. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')



    elif turno == 2:
        if turno_maq<=750:
            print('Maquina: Es mi turno. Envido')
            J1=input(f'Tenes un envido de {envidoJ1}. Queres envido, no queres, o queres envido envido? ')
            J1 = J1.lower()
            if J1 == 'quiero':
                if envidoJ1>envidoJ2:
                    puntosJ1+=3
                    print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                elif envidoJ2>envidoJ1:
                    puntosJ2+=3
                    print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                elif envidoJ1==envidoJ2:
                    puntosJ1+=2
                    print(f'Tenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
            elif J1 == 'no quiero':
                puntosJ2+=3
                print(f'No quisiste. Se le suman 3 a la maquina. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')

            elif J1 == 'envido envido':
                numero_random(turno_maq)
                if turno_maq <= 500:
                    print('Maquina: Quiero')
                    if envidoJ1>envidoJ2:
                        puntosJ1+=4
                        print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=4
                        print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ2+=4
                        print(f'Tenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                elif 500<turno_maq<=1000:
                    print('Maquina: No quiero.')
                    puntosJ1+=4
                    print(f'Ganaste. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')

        elif 750<turno_maq<=1000 and turno==2:
            print('Maquina: Es mi turno. Paso')
            turno = 1
            J1=input(f'Es tu turno. Tus castas son: {cartasJ1[0][0]} de {cartasJ1[0][1]}, {cartasJ1[1][0]} de {cartasJ1[1][1]}, y {cartasJ1[2][0]} de {cartasJ1[2][1]}. Tenes un envido de {envidoJ1}. Canta envido o pasa. ')
            J1= J1.lower()
            if J1 == 'envido':
                if turno_maq<= 600 and turno==1:
                    print('Maquina: Quiero.')
                    if envidoJ1>envidoJ2:
                        puntosJ1+=3
                        print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=3
                        print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ1+=3
                        print(f'Tenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                
                elif 600<turno_maq<=900 and turno==1:
                    print('Maquina: No quiero.')
                    puntosJ1+=3
                    print(f'Ganaste. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                    
                elif 901<turno_maq<=1000 and turno==1:
                    J1=input('Maquina: Envido envido. ')
                    J1= J1.lower()
                    if J1 == 'quiero':
                        if envidoJ1>envidoJ2:
                            puntosJ1+=4
                            print(f'Ganaste. La maquina tenia {envidoJ2}. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                        elif envidoJ2>envidoJ1:
                            puntosJ2+=4
                            print(f'Perdiste. La maquina tenia {envidoJ2}. Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                        elif envidoJ1==envidoJ2:
                            puntosJ1+=4
                            print(f'Tenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1}, contra {puntosJ2} de la maquina.')
                    elif J1 == 'no quiero':
                        puntosJ2+=3
                        print(f'Ahora la maquina tiene {puntosJ2}, contra {puntosJ1} tuyos.')
                

                


print('Game Over.')

























