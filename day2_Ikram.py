#It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

    #forward X increases the horizontal position by X units.
    #down X increases the depth by X units.
    #up X decreases the depth by X units.
#


fitxer_entrada = open("Day2_Ikram.txt","r")
hos_1=0
hos_2= 0
for line in fitxer_entrada.read().splitlines():
	direccio, valor = line.split()
	if direccio[0] == 'f':
		hos_1 += int(valor)
	elif direccio[0] == 'u':
		hos_2 -= int(valor)
	elif direccio[0] == 'd':
		hos_2 += int(valor)
        
print(hos_1 * hos_2)
fitxer_entrada.close()