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

    rndcarta1=random.choice(cartas) 
    rndcarta2=random.choice(cartas)
    rndcarta3=random.choice(cartas)
    tipodecarta1=random.randint(1, 4)
    tipodecarta2=random.randint(1, 4)
    tipodecarta3=random.randint(1, 4)
    
    #rndcarta es el numero de la carta
    #tipodecarta es el palo de la carta
    
    numcartaj1=[]
    numcartaj2=[]
    numcartaj3=[]
    carta1=''
    carta2=''
    carta3=''
    numcartaj1.extend([tipodecarta1, rndcarta1])
    numcartaj2.extend([tipodecarta2, rndcarta2])
    numcartaj3.extend([tipodecarta3, rndcarta3])
    
    
    #CARTA 1
    if 1 == tipodecarta1:
        carta1=str(rndcarta1) +' de oro'
    elif 2 == tipodecarta1:
        carta1=str(rndcarta1) +' de espada'
    elif 3 == tipodecarta1:
        carta1=str(rndcarta1) +' de copa'
    elif 4 == tipodecarta1:
        carta1=str(rndcarta1) +' de basto'
    
    #CARTA 2
    if 1 == tipodecarta2:
        carta2=str(rndcarta2) +' de oro'
    elif 2 == tipodecarta2:
        carta2=str(rndcarta2) +' de espada'
    elif 3 == tipodecarta2:
        carta2=str(rndcarta2) +' de copa'
    elif 4 == tipodecarta2:
       carta2=str(rndcarta2) +' de basto'
    
    #CARTA 3
    if 1 == tipodecarta3:
        carta3=str(rndcarta3) +' de oro'
    elif 2 == tipodecarta3:
       carta3=str(rndcarta3) +' de espada'
    elif 3 == tipodecarta3:
        carta3=str(rndcarta3) +' de copa'
    elif 4 == tipodecarta3:
       carta3=str(rndcarta3) +' de basto'
       
    #CALCULO ENVIDO
    envidojug=0
    if tipodecarta1 == tipodecarta2: 
        envidojug=20
        if rndcarta1 not in (10, 11, 12) and rndcarta2 not in (10, 11, 12):
            envidojug +=rndcarta1+rndcarta2
           # print('Tenes un envido de ',envidojug)
        
    elif tipodecarta1 == tipodecarta3:
        envidojug=20
        if rndcarta1 not in (10, 11, 12) and rndcarta3 not in (10, 11, 12):
            envidojug +=rndcarta1+rndcarta3
            #print('Tenes un envido de ',envidojug)
    
    elif tipodecarta2==tipodecarta3:
        envidojug=20
        if rndcarta3 not in (10, 11, 12) and rndcarta2 not in (10, 11, 12):
            envidojug +=rndcarta2+rndcarta3
            #print('Tenes un envido de ',envidojug)
    else:
        envidojug=max(rndcarta1, rndcarta2, rndcarta3)
        
    
    
    
    if turno == 1:
        turnohum=input('Es tu turno. Tus cartas son un ' + str(carta1) +', '+ str(carta2) +', '+ str(carta3) + '. Tenes un envido de ' + str(envidojug) + '. Canta envido o pasa. ')
        if turnohum == 'Envido' or 'envido':
            print("gola")
    elif turno == 2:
        envido=random.randint(1, 2)
        if envido==1:
            envidomaq=input('Es el turno de la maquina y te canto envido. Tus cartas son un ' + str(carta1) +', '+ str(carta2) +', '+ str(carta3) +'. Tenes un envido de ' + str(envidojug) + '.Queres envido? Queres pasar? o queres Envido Envido?.')
        elif envido == 2:
            noenvidomaq = input('Es el turno de la maquina y paso. Tus cartas son un ' + str(carta1) + ', ' + str(carta2) + ', ' + str(carta3) + '. Tenes un envido de ' + str(envidojug) + '. Canta envido o pasa. ')

else:
    print("hameover")
            
        
