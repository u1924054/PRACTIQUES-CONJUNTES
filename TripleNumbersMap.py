# escribir un programa que triplica tots el numeros d'una llista de int

#us de maps
lista = [1,2,3,4,5,6,7,8,9]
print (" La llista de la qual disposem orginal es ", lista)

#lambda -> funcio anonima

# lambda paramatros : expresion
    # Son funciones que pueden definir cualquier numero de parametros por una unica expresion
    # Se puede usar en cualquier lugar en el que una funcion sea requerida
    # Funciones restringidas al uso de una sola expresion
    
tripNum = map(lambda x: x + x + x, lista )
print("El resultat de la triplicacio mitjançant map es : \n")
print (list(tripNum))