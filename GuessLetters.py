# el jugador tiene que adivinar  la palabra "EVAPORATE"-
#Pre: Letra 
#Post: Si la letra es correcta se pondra en las la pantalla sino se dira que es incorrecto

print("Benvolgudes Hangman!")

lletra = input ("Digues la teva lletra: ")

evaporate = "evaporate"
if lletra in evaporate:
    print ("Hi es la lletra " + lletra)
else: print ("Torna-hi!")



