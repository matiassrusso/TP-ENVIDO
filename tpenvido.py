# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:57:05 2023

@author: matia
"""

puntosj1=0
puntosj2=0

while puntosj1 < 15 and puntosj2 < 15:
    import random
    cartas = [c for c in range(1, 12) if c not in [8, 9]]
    turno=random.randint(1, 2)

    #la base arranca aca
    #J1 es el jugador 1, el humano
    #J2 es la maquina


    #CODIGO JUGADOR 1

    numcarta1_J1=random.choice(cartas) 
    numcarta2_J1=random.choice(cartas)
    numcarta3_J1=random.choice(cartas)
    rndpalocarta1_J1=random.randint(1, 4)
    rndpalocarta2_J1=random.randint(1, 4)
    rndpalocarta3_J1=random.randint(1, 4)
    
    #rndcarta es el numero de la carta
    #tipodecarta es el palo de la carta
    
    codcarta1_J1=[]
    codcarta2_J1=[]
    codcarta3_J1=[]
    carta1_J1=''
    carta2_J1=''
    carta3_J1=''
    codcarta1_J1.extend([rndpalocarta1_J1, numcarta1_J1])
    codcarta2_J1.extend([rndpalocarta2_J1, numcarta2_J1])
    codcarta3_J1.extend([rndpalocarta3_J1, numcarta3_J1])
    
    
    #CARTA 1
    if 1 == rndpalocarta1_J1:
        carta1_J1=str(numcarta1_J1) +' de oro'
    elif 2 == rndpalocarta1_J1:
        carta1_J1=str(numcarta1_J1) +' de espada'
    elif 3 == rndpalocarta1_J1:
        carta1_J1=str(numcarta1_J1) +' de copa'
    elif 4 == rndpalocarta1_J1:
        carta1_J1=str(numcarta1_J1) +' de basto'
    
    #CARTA 2
    if 1 == rndpalocarta2_J1:
        carta2_J1=str(numcarta2_J1) +' de oro'
    elif 2 == rndpalocarta2_J1:
        carta2_J1=str(numcarta2_J1) +' de espada'
    elif 3 == rndpalocarta2_J1:
        carta2_J1=str(numcarta2_J1) +' de copa'
    elif 4 == rndpalocarta2_J1:
       carta2_J1=str(numcarta2_J1) +' de basto'
    
    #CARTA 3
    if 1 == rndpalocarta3_J1:
        carta3_J1=str(numcarta3_J1) +' de oro'
    elif 2 == rndpalocarta3_J1:
       carta3_J1=str(numcarta3_J1) +' de espada'
    elif 3 == rndpalocarta3_J1:
        carta3_J1=str(numcarta3_J1) +' de copa'
    elif 4 == rndpalocarta3_J1:
       carta3_J1=str(numcarta3_J1) +' de basto'
       
    #CALCULO ENVIDO
    envido_J1=0
    if rndpalocarta1_J1 == rndpalocarta2_J1: 
        envido_J1=20
        if numcarta1_J1 not in (10, 11, 12) and numcarta2_J1 not in (10, 11, 12):
            envido_J1 +=numcarta1_J1+numcarta2_J1
           # print('Tenes un envido de ',envido_J1)
        
    elif rndpalocarta1_J1 == rndpalocarta3_J1:
        envido_J1=20
        if numcarta1_J1 not in (10, 11, 12) and numcarta3_J1 not in (10, 11, 12):
            envido_J1 +=numcarta1_J1+numcarta3_J1
            #print('Tenes un envido de ',envido_J1)
    
    elif rndpalocarta2_J1==rndpalocarta3_J1:
        envido_J1=20
        if numcarta3_J1 not in (10, 11, 12) and numcarta2_J1 not in (10, 11, 12):
            envido_J1 +=numcarta2_J1+numcarta3_J1
            #print('Tenes un envido de ',envido_J1)
    else:
        envido_J1=max(numcarta1_J1, numcarta2_J1, numcarta3_J1)


    #CODIGO JUGADOR 2

    numcarta1_J2=random.choice(cartas) 
    numcarta2_J2=random.choice(cartas)
    numcarta3_J2=random.choice(cartas)
    rndpalocarta1_J2=random.randint(1, 4)
    rndpalocarta2_J2=random.randint(1, 4)
    rndpalocarta3_J2=random.randint(1, 4)
    
    #rndcarta es el numero de la carta
    #tipodecarta es el palo de la carta
    
    codcarta1_J2=[]
    codcarta2_J2=[]
    codcarta3_J2=[]
    carta1_J2=''
    carta2_J2=''
    carta3_J2=''
    codcarta1_J2.extend([rndpalocarta1_J2, numcarta1_J2])
    codcarta2_J2.extend([rndpalocarta2_J2, numcarta2_J2])
    codcarta3_J2.extend([rndpalocarta3_J2, numcarta3_J2])
    
    
    #CARTA 1
    if 1 == rndpalocarta1_J2:
        carta1_J2=str(numcarta1_J2) +' de oro'
    elif 2 == rndpalocarta1_J2:
        carta1_J2=str(numcarta1_J2) +' de espada'
    elif 3 == rndpalocarta1_J2:
        carta1_J2=str(numcarta1_J2) +' de copa'
    elif 4 == rndpalocarta1_J2:
        carta1_J2=str(numcarta1_J2) +' de basto'
    
    #CARTA 2
    if 1 == rndpalocarta2_J2:
        carta2_J2=str(numcarta2_J2) +' de oro'
    elif 2 == rndpalocarta2_J2:
        carta2_J2=str(numcarta2_J2) +' de espada'
    elif 3 == rndpalocarta2_J2:
        carta2_J2=str(numcarta2_J2) +' de copa'
    elif 4 == rndpalocarta2_J2:
       carta2_J2=str(numcarta2_J2) +' de basto'
    
    #CARTA 3
    if 1 == rndpalocarta3_J2:
        carta3_J2=str(numcarta3_J2) +' de oro'
    elif 2 == rndpalocarta3_J2:
       carta3_J2=str(numcarta3_J2) +' de espada'
    elif 3 == rndpalocarta3_J2:
        carta3_J2=str(numcarta3_J2) +' de copa'
    elif 4 == rndpalocarta3_J2:
       carta3_J2=str(numcarta3_J2) +' de basto'
       
    #CALCULO ENVIDO J2
    envido_J2=0
    if rndpalocarta1_J2 == rndpalocarta2_J2: 
        envido_J2=20
        if numcarta1_J2 not in (10, 11, 12) and numcarta2_J2 not in (10, 11, 12):
            envido_J2 +=numcarta1_J2+numcarta2_J2
           # print('Tenes un envido de ',envido_J2)
        
    elif rndpalocarta1_J2 == rndpalocarta3_J2:
        envido_J2=20
        if numcarta1_J2 not in (10, 11, 12) and numcarta3_J2 not in (10, 11, 12):
            envido_J2 +=numcarta1_J2+numcarta3_J2
            #print('Tenes un envido de ',envido_J2)
    
    elif rndpalocarta2_J2==rndpalocarta3_J2:
        envido_J2=20
        if numcarta3_J2 not in (10, 11, 12) and numcarta2_J2 not in (10, 11, 12):
            envido_J2 +=numcarta2_J2+numcarta3_J2
            #print('Tenes un envido de ',envido_J2)
    else:
        envido_J2=max(numcarta1_J2, numcarta2_J2, numcarta3_J2)


    #la base termina aca
        
    
    envidornd_J2=random.randint(1,1000)
    quiero_J2 = (envidornd_J2 <= 500 )
    no_quiero_J2 = (500< envidornd_J2 <= 825)
    paso_J2 = (825<envidornd_J2<=1000)

    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    # Agregar la condición de número primo
    envenv_J2 = es_primo(envidornd_J2)
        
    #JUEGO
    total=envido_J1 - envido_J2

    if turno == 1: #turno es un random que esta arriba
        turno_J1=input('Es tu turno. Tus cartas son un ' + str(carta1_J1) +', '+ str(carta2_J1) +', '+ str(carta3_J1) + '. Tenes un envido de ' + str(envido_J1) + '. Canta envido o pasa. ')
        if turno_J1 == 'Envido' or 'envido':
            if quiero_J2 == True: #Aca la maquina accede al envido
                if envenv_J2==True: #Aca la maquina pide jugar envido envido. Este es el codigo de Envido envido
                    print('Computadora: Envido Envido.')
                    envenv_J1=input(' ')
                    if envenv_J1 == 'Quiero' or 'quiero': #ACA EL JUGADOR JUEGA ENVIDO ENVIDO
                        if total > 0:
                            puntosj1+=4
                            print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')                        
                        elif total < 0:
                            puntosj2+=4
                            print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                        elif total == 0:
                            puntosj1 +=4
                            print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')

                    elif envenv_J1 =='No quiero' or 'no quiero': #ACA EL JUGADOR RECHAZA EL ENVIDO ENVIDO
                        puntosj2 += 3
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                       

                elif envenv_J2==False: #ACA LA MAQUINA JUEGA ENVIDO NORMAL #Codigo Envido normal    
                    print('Computadora: Quiero')
                    if total > 0:
                        puntosj1+=3
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif total < 0:
                        puntosj2+=3
                        print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif total == 0:
                        puntosj1 +=3
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                        
            elif no_quiero_J2 == True: #ACA LA MAQUINA RECHAZA EL ENVIDO NORMAL
                puntosj1+=3
                print('Ganaste. Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')

        elif turno_J1=='Paso' or 'paso': #ACA EL JUGADOR PASO EL TURNO.
            if quiero_J2==True: #ACA LA MAQUINA PASA A SER MANO
                print('Computadora: Envido.')
                envJ1=input(' ')
                if envJ1 == 'Quiero' or 'quiero': #ACA EL JUGADOR JUEGA ENVIDO NORMAL
                    if total > 0:
                        puntosj1+=3
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif total < 0:
                        puntosj2+=3
                        print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif total == 0:
                        puntosj1 +=3
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')

                elif envJ1 == 'No quiero' or 'no quiero': #ACA EL JUGADOR RECHAZA EL ENVIDO
                    puntosj2+=3
                    print('Ganaste. Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')

                elif envJ1 == 'Envido' or 'Envido envido' or 'envido' or 'Envido Envido' or 'envido envido': #ACA EL JUGADOR CANTA ENVIDO ENVIDO
                    if quiero_J2 == True:
                        print('Computadora: Quiero.')
                        if total > 0:
                            puntosj1+=4
                            print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')                        
                        elif total < 0:
                            puntosj2+=4
                            print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                        elif total == 0:
                            puntosj1 +=4
                            print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif no_quiero_J2==True:
                        print('Computadora: No quiero.')
                        puntosj1+=3
                        print('Ganaste. Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
        elif quiero_J2 == False:
            print('Computadora: Paso')
            print('La computadora paso. Se te suma un punto.')
            puntosj1+=1
            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')


    elif turno == 2:
        if quiero_J2==True: #ACA LA MAQUINA JUGO EL TURNO
            cantenv_J2=input('Es el turno de la maquina y te canto envido. Tus cartas son un ' + str(carta1_J1) +', '+ str(carta2_J1) +', '+ str(carta3_J1) +'. Tenes un envido de ' + str(envido_J1) + '.Queres envido? Queres pasar? o queres Envido Envido?. ')
            if cantenv_J2 == 'Quiero' or 'quiero': #ACA EL JUGADOR JUEGA ENVIDO NORMAL
                    if total > 0:
                        puntosj1+=3
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif total < 0:
                        puntosj2+=3
                        print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif total == 0:
                        puntosj1 +=3
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')

            elif cantenv_J2 == 'No quiero' or 'no quiero': #ACA EL JUGADOR RECHAZA EL ENVIDO
                    puntosj2+=3
                    print('Ganaste. Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')

            elif cantenv_J2 == 'Envido' or 'Envido envido' or 'envido' or 'Envido Envido' or 'envido envido': #ACA EL JUGADOR CANTA ENVIDO ENVIDO
                if quiero_J2 == True:
                    print('Computadora: Quiero.')
                    if total > 0:
                        puntosj1+=4
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')                        
                    elif total < 0:
                        puntosj2+=4
                        print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                    elif total == 0:
                        puntosj1 +=4
                        print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                        print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                elif no_quiero_J2==True:
                    print('Computadora: No quiero.')
                    puntosj1+=3
                    print('Ganaste. Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')        


        elif paso_J2 == True: #ACA LA MAQUINA PASO DE TURNO
            pasomaq_J2 = input('Es el turno de la maquina y paso. Tus cartas son un ' + str(carta1_J1) + ', ' + str(carta2_J1) + ', ' + str(carta3_J1) + '. Tenes un envido de ' + str(envido_J1) + '. Canta envido o pasa. ')
            if pasomaq_J2 == 'Envido' or 'envido':
                if quiero_J2 == True: #Aca la maquina accede al envido
                    if envenv_J2==True: #Aca la maquina pide jugar envido envido. Este es el codigo de Envido envido
                        print('Computadora: Envido Envido.')
                        envenv_J1=input(' ')
                        if envenv_J1 == 'Quiero' or 'quiero': #ACA EL JUGADOR JUEGA ENVIDO ENVIDO
                            if total > 0:
                                puntosj1+=4
                                print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                                print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')                        
                            elif total < 0:
                                puntosj2+=4
                                print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                                print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                            elif total == 0:
                                puntosj1 +=4
                                print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                                print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')

                        elif envenv_J1 =='No quiero' or 'no quiero': #ACA EL JUGADOR RECHAZA EL ENVIDO ENVIDO
                            puntosj2 += 3
                            print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                        

                    elif envenv_J2==False: #ACA LA MAQUINA JUEGA ENVIDO NORMAL #Codigo Envido normal    
                            print('Computadora: Quiero')
                            if total > 0:
                                puntosj1+=3
                                print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                                print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                            elif total < 0:
                                puntosj2+=3
                                print('Perdiste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                                print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                            elif total == 0:
                                puntosj1 +=3
                                print('Ganaste. La computadora tenia ',envido_J2,'de envido, contra ',envido_J1,' tuyos.')
                                print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                            
                elif no_quiero_J2 == True: #ACA LA MAQUINA RECHAZA EL ENVIDO NORMAL
                    print('Computadora: No quiero')                                
                    puntosj1+=3
                    print('Ganaste. Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')
                else:
                    print('ASDASDADSD')

            elif pasomaq_J2=='Paso' or 'paso': #ACA EL JUGADOR PASO EL TURNO.
                print('Pasaron los 2. Se le suma 1 punto a la computadora.')
                puntosj2+=1
                print('Ahora vos tenes ',puntosj1,' puntos y la maquina tiene ',puntosj2,' puntos.')




print("Game over")
            
        
