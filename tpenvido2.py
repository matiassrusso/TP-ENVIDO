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


def envido():
    if palo_carta() in cartasJ1[0] == palo_carta() in cartasJ1[1]:
        print('hola')


num_carta()
palo_carta()
print(cartasJ1)
print(cartasJ2)
print(cartasJ1[0][0])
print(f'Carta usuario: {cartasJ1[0][0]} de {cartasJ1[0][1]}')








