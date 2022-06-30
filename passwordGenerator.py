#password generator --> strong passwords 
#password de 8 elements
import string, random

# ord --> retorna un int que representa el caràcter que se li ha passat
#random.int --> retorna un numero que va entre variables

#randlowercase = chr(random.randint(ord('a'), ord('z')))
#randuppercase = chr(random.randint(ord('A'), ord('Z')))
#number = random.randint(0,9)

grauSeguretatPassword = input('\nCom vols la contrasenya? D (debil) F (forta) FI per acabar: \n')
while grauSeguretatPassword != "FI":
    
    if grauSeguretatPassword == "F":

        print("La contrasenya que s'ha generat es la seguent:")
        randomStrongPassword = ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase +  string.digits + string.punctuation ) for n in 
        range(10)])
        print(randomStrongPassword)

    elif grauSeguretatPassword == "D": 
        randomWeakPassword = ''.join([random.choice(string.ascii_lowercase + string.digits ) for n in 
        range(10)])
        print(randomWeakPassword)

    else:
        print('Entrada incorrecta. Entra una opcio vàlida.\n')
    grauSeguretatPassword = input('\nCom vols la contrasenya? D (debil) F (forta) FI per acabar:\n')


print('Final del programa')