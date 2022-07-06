# --- Day 3: Binary Diagnostic ---

"""
    You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 
    The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
"""
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position

"""
    L'informe de diagnòstic (l'entrada del vostre trencaclosques) consisteix en una llista de números binaris que, quan es descodifiquen correctament, 
    us poden dir moltes coses útils sobre les condicions del submarí. El primer paràmetre a comprovar és el consum d'energia .
"""
fitxerEntrada = open ("day3_ikram.txt","r")
llista = fitxerEntrada.read().splitlines()

ratio_primer = [0] * len(llista[0])
ratio_segon = [0] * len(llista[0])

for i in range(len(llista[0])):
	zero = 0
	one = 0
	for j in range(len(llista)):
		zero += llista[j][i] == '0'
		one += llista[j][i] == '1'
	if zero > one:
		ratio_primer[i] = '0'
		ratio_segon[i] = '1'
	elif one > zero:
		ratio_primer[i] = '1'
		ratio_segon[i] = '0'
ratio_dec1 = int(''.join(ratio_primer), 2)
ratio_dec2 = int(''.join(ratio_segon), 2)
print(ratio_dec1 * ratio_dec2)
fitxerEntrada.close()

