'''
 Se requiere un script en python que permita crear una
 carrera numerica con dos players.
 la carrera inicia en la posicion CERO y finaliza en la posicion 100
 El juego se realiza por default con 2 jugadores
 El jugador que llegue pimero ala meta (posicion 100 sera el ganador)
 Si un jugador ganara 3 pares consecutivos en el lanzamiento de los dados
 sera directamente ganador
 repite tiro si y solo si saca PAR.

'''

#randint => genera valores numericos enteros {Z}(+,-)
#uniform => Genera valores numericos reales {R} (+,-)

import os
from  random import randint, uniform

os.system("clear")

dice1 = randint(1,6)
dice2 = randint(1,6)

print("Dice 1: ", dice1)
print("Dice 2: ", dice2)

