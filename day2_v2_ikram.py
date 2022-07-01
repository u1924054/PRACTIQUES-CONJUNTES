
""" down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
"""

fitxer_entrada = open("Day2_Ikram.txt","r")
hos_1=0
hos_2= 0
aux =0 
for line in fitxer_entrada.read().splitlines():
    direccio, valor = line.split()
    if direccio[0] == 'f':
        hos_1 += int(valor)
        hos_2 += aux * int(valor)
    elif direccio[0] == 'u':
        aux -= int(valor)
    elif direccio[0] == 'd':
        aux += int(valor)
print(hos_1 * hos_2)
fitxer_entrada.close()