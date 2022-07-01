# Sonar Sweep

# Mes informacio de l'enunciat a : https://adventofcode.com/2021/day/1

#primer obrim el fitxer on tenim el report en mode lectura


#crear una llista que conté cada linia del fixer
# Open the file
fitxer = open('day1_Ikram.txt', 'r')
# create a list of the data within the file
list_mesures = list(map(int, fitxer.read().splitlines()))
result = 0

resultat = 0

# ara es crea una variable que contingui la suma de les tres primeres mesures.
# ara es fara un recorregut pel fitxer amb l'ajut del tamany d'aquest, es calculara l'actual arbre de mesura "sliding window"
tamany = len(list_mesures)
for i in range(tamany-1):
    if (list_mesures[i] < list_mesures[i+1]):
        resultat +=1
print (resultat)
fitxer.close()
