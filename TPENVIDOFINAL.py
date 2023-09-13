import random

cartasJ1=[[],[],[]]         #SON LOS ARRAYS PARA CADA CARTA. ACA GUARDO LO QUE CREO EN LAS FUNCIONES

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
    array_carta[2].clear()              #ACA BORRO LA CARTA ANTERIOR, PARA GENERAR UNA NUEVA

    array_carta[0].extend([num_carta(), palo_carta()])
    array_carta[1].extend([num_carta(), palo_carta()])
    while array_carta[0] == array_carta[1]:                 #CON ESTE "sistema" CHEQUEO QUE NO REPITA LA CARTA, Y LA GUARDO EN EL ARRAY
        array_carta[1].clear()
        array_carta[1].extend([num_carta(), palo_carta()])

    array_carta[2].extend([num_carta(), palo_carta()])
    while array_carta[0] == array_carta[2] or array_carta[1] == array_carta[2]:
        array_carta[2].clear()
        array_carta[2].extend([num_carta(), palo_carta()])

pre_envidoJ1=0              #una variable para guardar un numero. es bastante irrelevante pero sirve
pre_envidoJ2=0


def envido(array_carta, int_envido):            #SISTEMA DE CALCULO DEL ENVIDO
    
    if array_carta[2][1] == array_carta[1][1] == array_carta[0][1]:     #SITUACION FLOR
        int_envido=20
        cartas_iguales=[array_carta[0][0], array_carta[1][0], array_carta[2][0]]        #guardo los numeros de las 3 cartas en un array
        if max(cartas_iguales) >= 10:           #si la carta mas grande es mayor o igual a 10, la saco del array
            cartas_iguales.remove(max(cartas_iguales))          #uso el remove para que me queden solo 2 cartas.
        else:
            cartas_iguales.remove(min(cartas_iguales))          #si no hay ninguna mayor o igual a 10, saco la mas chica
        for numero in cartas_iguales:
            if numero not in (10,11,12):        #si no hay ninguno mayor o igual a 10, sumo las cartas.
                int_envido+=numero

    elif array_carta[0][1]== array_carta[1][1]:      #SI EL PALO DE LA PRIMERA CARTA ES IGUAL AL PALO DE LA SEGUNDA
        int_envido=20
        cartas_iguales=[array_carta[0][0],array_carta[1][0]]
        for numero in cartas_iguales:
            if numero not in (10,11,12):         #si no hay ninguno mayor o igual a 10, sumo las cartas.
                int_envido+=numero


    elif array_carta[0][1] == array_carta[2][1]:    #SI EL PALO DE LA PRIMERA CARTA ES IGUAL AL PALO DE LA TERCERA
        int_envido=20
        cartas_iguales=[array_carta[0][0],array_carta[2][0]]
        for numero in cartas_iguales:
            if numero not in (10,11,12):
                int_envido+=numero
        

    elif array_carta[2][1] == array_carta[1][1]:    #SI EL PALO DE LA TERCERA ES IGUAL AL PALO DE LA SEGUNDA
        int_envido=20
        cartas_iguales=[array_carta[2][0],array_carta[1][0]]
        for numero in cartas_iguales:
            if numero not in (10,11,12):
                int_envido+=numero

   
    elif array_carta[2][1] != array_carta[1][1] != array_carta[0][1]:     #SITUACION TODOS DISTINTOS
        templist=[]     #creo esta lista para ordenar las cartas y elegir la mas grande, sacando de 10 para arriba
        templist.extend([array_carta[2][0], array_carta[1][0], array_carta[0][0]])
        templist.sort(reverse=True)
        if templist[0] not in (10,11,12):
            int_envido+=templist[0]
        elif templist[1] not in (10, 11, 12):
            int_envido+=templist[1]
        elif templist[2] not in (10, 11,12):
            int_envido+=templist[2]
        else:
            int_envido=0        #si tengo 3 mayores a 10, no tengo envido

    int_envido = int(int_envido)            #esto es para hacer que se muestre como un entero, y no como lista
    return int_envido

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




def numero_random(intmaq):          #funcion para el sistema de random de la maquina.
    intmaq=0
    intmaq=random.randint(1, 1000)
    return intmaq
    
#Juego
turno_maq=0
puntosJ1=0
puntosJ2=0
while True:     #loop para la cantidad de puntos a jugar (ej extra)
    try:
        puntos_totales = int(input("Hola! Este es un juego de envido. Es contra la máquina. Hasta cuántos puntos quieres jugar? "))
        if puntos_totales <= 0:  #si el numero es menor que 0, se repite
            print("Por favor, ingresa un número de puntos mayor que cero.")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un número de puntos válido.")  #si no es un entero, se repite

print(f'Perfecto. El primero en llegar a {puntos_totales} puntos gana. ')
input("Presiona Enter para continuar...")
print("Las reglas son las siguientes:\nCuando sea tu turno, escribi 'envido' para cantar envido, y 'paso' para pasar el turno.")
input("Presiona Enter para continuar...")
print("Si no es tu turno, y arranca la maquina, los comandos son los siguientes:\n'quiero' para aceptar el envido.\n'no quiero' para rechazar el envido.\nY 'envido' para jugar envido envido. Suerte.")

turno=0 #variable de turnos. se le suma 1 por turno y va cambiando


while puntosJ1 < puntos_totales and puntosJ2 < puntos_totales:      #loop del juego
    carta(cartasJ1) #genera las cartas del Jugador
    carta(cartasJ2)
    numero_random(turno_maq) #elije un numero random para la maquina
    envidoJ1= envido(cartasJ1,pre_envidoJ1) #calcula el envido del jugador
    envidoJ2 = envido(cartasJ2,pre_envidoJ2)

    if turno%2 == 0:        #si el numero es par, es el turno del J1
        turno+=1 #ahora el numero es impar. cambia de turno
        J1=input(f'\nEs tu turno. Tus cartas son: {cartasJ1[0][0]} de {cartasJ1[0][1]}, {cartasJ1[1][0]} de {cartasJ1[1][1]}, y {cartasJ1[2][0]} de {cartasJ1[2][1]}. Tenes un envido de {envidoJ1}. Canta envido o pasa. ')  #input del jugador
        J1= J1.lower() #el input ahora esta en minusculas
        while J1 != 'envido' and J1 != 'paso':
            J1=input('\n Comando invalido. Proba de nuevo. ')  #si lo escrito es incorrecto, te pide que lo escribas de nuevo (ej extra)
            J1= J1.lower()

        if J1 == 'envido': #situacion si el jugador juega pide envido normal
            if envidoJ2>=25:  #si el envido es mayor a 25, la maquina va a querer
                if envidoJ2>28: #pero si el envido es mayor a 28, la maquina va a querer jugar envido envido
                    J1=input('\nMaquina: envido. ')
                    J1= J1.lower()
                    while J1 != 'quiero' and J1 != 'no quiero':
                        J1=input('\n Comando invalido. Proba de nuevo. ')
                        J1= J1.lower()

                    if J1 == 'quiero':
                        if envidoJ1>envidoJ2:
                            puntosJ1+=4
                            print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                        elif envidoJ2>envidoJ1:
                            puntosJ2+=4
                            print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                        elif envidoJ1==envidoJ2:
                            puntosJ1+=4
                            print(f'\nTenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    elif J1 == 'no quiero':
                        puntosJ2+=3
                        print(f'\nAhora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                else:
                    print('\nMaquina: Quiero.')
                    if envidoJ1>envidoJ2:
                        puntosJ1+=3
                        print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=3
                        print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ1+=3
                        print(f'\nTenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                
            elif 600<turno_maq<=900 or envidoJ2 <25:
                print('\nMaquina: No quiero.')
                puntosJ1+=3
                print(f'\nGanaste. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                
            elif 901<turno_maq<=1000 or envidoJ2>28:
                J1=input('\nMaquina: envido. ')
                J1= J1.lower()
                while J1 != 'quiero' and J1 != 'no quiero':
                    J1=input('\n Comando invalido. Proba de nuevo. ')
                    J1= J1.lower()

                if J1 == 'quiero':
                    if envidoJ1>envidoJ2:
                        puntosJ1+=4
                        print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=4
                        print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ1+=4
                        print(f'\nTenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                elif J1 == 'no quiero':
                    puntosJ2+=3
                    print(f'\nAhora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
        
        elif J1 == 'paso':
            #numero_random(turno_maq)
            #turno = 2
            if turno_maq<=750 or envidoJ2>=25:
                print('\nMaquina: Bueno ahora es mi turno. Envido')
                J1=input(f'\nTenes un envido de {envidoJ1} de envido. Queres envido, no queres, o queres envido envido? ')
                J1 = J1.lower()
                while J1 != 'quiero' and J1 != 'no quiero' and J1 != 'envido':
                    J1=input('\n Comando invalido. Proba de nuevo. ')
                    J1= J1.lower()

                if J1 == 'quiero':
                    if envidoJ1>envidoJ2:
                        puntosJ1+=3
                        print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=3
                        print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ1+=2
                        print(f'\nTenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                elif J1 == 'no quiero':
                    puntosJ2+=1
                    print(f'\nNo quisiste. Se le suma 1 a la maquina. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')

                elif J1 == 'envido':
                    numero_random(turno_maq)
                    if envidoJ2>28:
                        print('\nMaquina: Quiero')
                        if envidoJ1>envidoJ2:
                            puntosJ1+=4
                            print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                        elif envidoJ2>envidoJ1:
                            puntosJ2+=4
                            print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                        elif envidoJ1==envidoJ2:
                            puntosJ2+=4
                            print(f'\nTenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    elif envidoJ2<27:
                        print('\nMaquina: No quiero.')
                        puntosJ1+=4
                        print(f'\nGanaste. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
            elif 750<turno_maq<=1000 or envidoJ2<22:
                print('\nMaquina: Paso.')
                print(f'\nLa maquina paso. No se le suman puntos a nadie. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')



    else:
        turno+=1
        if turno_maq<=750 or envidoJ2 >=26:
            print('\nMaquina: Es mi turno. Envido')
            J1=input(f'\nTus cartas son: {cartasJ1[0][0]} de {cartasJ1[0][1]}, {cartasJ1[1][0]} de {cartasJ1[1][1]}, y {cartasJ1[2][0]} de {cartasJ1[2][1]}. Tenes un envido de {envidoJ1}. Queres envido, no queres, o queres envido envido? ')
            J1 = J1.lower()
            while J1 != 'envido' and J1 != 'quiero' and J1 != 'no quiero':
                J1=input('\n Comando invalido. Proba de nuevo. ')
                J1= J1.lower()
            if J1 == 'quiero':
                if envidoJ1>envidoJ2:
                    puntosJ1+=3
                    print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                elif envidoJ2>envidoJ1:
                    puntosJ2+=3
                    print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                elif envidoJ1==envidoJ2:
                    puntosJ2+=3
                    print(f'\nTenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
            elif J1 == 'no quiero':
                puntosJ2+=1
                print(f'\nNo quisiste. Se le suma 1 a la maquina. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')

            elif J1 == 'envido':
                numero_random(turno_maq)
                if envidoJ2>=28:
                    print('\nMaquina: Quiero')
                    if envidoJ1>envidoJ2:
                        puntosJ1+=4
                        print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    elif envidoJ2>envidoJ1:
                        puntosJ2+=4
                        print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                    elif envidoJ1==envidoJ2:
                        puntosJ2+=4
                        print(f'\nTenian el mismo envido. Gano la maquina por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                elif envidoJ2<28:
                    print('\nMaquina: No quiero.')
                    puntosJ1+=3
                    print(f'\nGanaste. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')

        elif 750<turno_maq<=1000 or envidoJ2<21:
            print('\nMaquina: Es mi turno. Paso')
            
            J1=input(f'\nEs tu turno. Tus cartas son: {cartasJ1[0][0]} de {cartasJ1[0][1]}, {cartasJ1[1][0]} de {cartasJ1[1][1]}, y {cartasJ1[2][0]} de {cartasJ1[2][1]}. Tenes un envido de {envidoJ1}. Canta envido o pasa. ')
            J1= J1.lower()
            while J1 != 'envido' and J1 != 'paso':
                J1=input('\n Comando invalido. Proba de nuevo. ')
                J1= J1.lower()
            if J1 == 'envido':
                if turno_maq<= 600 or envidoJ2>=25:
                    if envidoJ2>=28:
                        J1=input('\nMaquina: envido. ')
                        J1= J1.lower()
                        if J1 == 'quiero':
                            if envidoJ1>envidoJ2:
                                puntosJ1+=4
                                print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                            elif envidoJ2>envidoJ1:
                                puntosJ2+=4
                                print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                            elif envidoJ1==envidoJ2:
                                puntosJ1+=4
                                print(f'\nTenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                        elif J1 == 'no quiero':
                            puntosJ2+=3
                            print(f'\nAhora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                    else:
                        print('\nMaquina: Quiero.')
                        if envidoJ1>envidoJ2:
                            puntosJ1+=3
                            print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                        elif envidoJ2>envidoJ1:
                            puntosJ2+=3
                            print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                        elif envidoJ1==envidoJ2:
                            puntosJ1+=3
                            print(f'\nTenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    
                elif 600<turno_maq<=900 or envidoJ2<25:
                    print('\nMaquina: No quiero.')
                    puntosJ1+=3
                    print(f'\nGanaste. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    
                elif 901<turno_maq<=1000 or envidoJ2>=28:
                    J1=input('\nMaquina: envido. ')
                    J1= J1.lower()
                    if J1 == 'quiero':
                        if envidoJ1>envidoJ2:
                            puntosJ1+=4
                            print(f'\nGanaste. La maquina tenia {envidoJ2} de envido. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                        elif envidoJ2>envidoJ1:
                            puntosJ2+=4
                            print(f'\nPerdiste. La maquina tenia {envidoJ2} de envido. Ahora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
                        elif envidoJ1==envidoJ2:
                            puntosJ1+=4
                            print(f'\nTenian el mismo envido. Ganaste por mano. Ahora tenes {puntosJ1} puntos, contra {puntosJ2} puntos de la maquina.')
                    elif J1 == 'no quiero':
                        puntosJ2+=3
                        print(f'\nAhora la maquina tiene {puntosJ2} puntos, contra {puntosJ1} puntos tuyos.')
            
            elif J1 == 'paso':
                print('Los dos pasaron. No se le suman puntos a nadie.')
                print(f'Ahora vos tenes {puntosJ1} puntos y la maquina tiene {puntosJ2} puntos.') 
                

                
print('\nGame Over.')

