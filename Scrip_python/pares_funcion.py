'''
Developer: jayala
Date: 14 aug 2021
Description: Scrit Python que permite identificar
numeros ingresados por consola atravez de una  funcion 
'''

import os 

os.system("clear")

#Functions

print("Ingrese primer numero: ")
n1 = int(input())

n2 = int(input("Ingrese  segundo numero: "))

if n1 > n2 :
    print("El mayor es: ", n1)
elif n1 < n2 :
    print("El mayor es: ", n2)
else :
    print("::: Los numeros son iguales :::")

