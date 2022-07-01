

#obrir fitxer i guardar tots els valors en un array
f=open("profunditats.txt","r")

profunditats = []
for linea in f:
    profunditats.append(linea)

print(profunditats)