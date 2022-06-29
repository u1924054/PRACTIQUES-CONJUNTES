
#generar un numero aleatori de l'1 al 9

import random

a= random.randint(1,9)

numero = int(input("Introdueix un numero aleatori de 1 a 9 tots dos inclosos: "))

if a== numero:
    print('Ho has adivinat.')
else:
    print ('No ho has adivinat')
    