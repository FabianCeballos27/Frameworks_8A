import os
from random import randint

#Functions
def dices() :
    status = True

    while status :     
        os.system("clear")
        dice1 = randint(0,100)
        dice2 = randint(0,100)
        result = (dice1+dice2)
        result2 = (result+ dice1+dice2)
        
        print("D1: ", dice1)
        print("D2: ", dice2)
        


        if dice1 + dice2 >= 100 :
            status = False
            print("->Llego a cien o más de cien. El lanzamiento ha finalizado:", result)
        else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")

            if result < 100:
                print("->Llego a cien o más de cien. El lanzamiento ha finalizado:", result2)
            else:
                print("FIN", result)

            

#Main
dices()
