#escriute una funcio que ordena una llista de numeros--> llista ordenada de petit a gran

#Pre: numero a cercar
#Post: retorna cert si s'ha trobat l'element a la llista fals, altrament

import random 
elelement = input("Entra un numero que volguis buscar a la llista \n")
llista = [1,8,34,67,98,120]
 # lista_ordenada = llista.sort()
def buscar_element(llista_ordenada,element_cerca):
    for i in llista_ordenada:
        if i == element_cerca:
            return True
    return False

print(buscar_element(llista,elelement))



 



