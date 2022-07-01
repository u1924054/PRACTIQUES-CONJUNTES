# exercici inicial per practicas l'us de dates

#calcular el  numero de dies que hi ha entre dues dates

from datetime import datetime


date_1 = datetime (2022,7,1)
date_2 = datetime (2022,9,7)

#result = date_2-date_1
#print (result)

#no obstant s'ha de tenir en compte quina es la major per evitar dies negatius

result = None

if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")